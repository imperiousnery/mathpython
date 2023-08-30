import requests
from bs4 import BeautifulSoup
from googlesearch import search
from concurrent.futures import ThreadPoolExecutor
import time
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextGenerationPipeline

# Function to get site summary
def get_site_summary(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")
    text = " ".join(p.get_text() for p in paragraphs)
    return text[:1000]

# Function to perform search on Google
def search_google(query, num_results):
    results = []
    for result in search(query, num_results=num_results):
        results.append(result)
        time.sleep(1)
    return results

# Function to perform search on Yahoo
def search_yahoo(query, start):
    url = f"https://search.yahoo.com/search?p={query}&b={start}&n=30"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [a['href'] for a in soup.select(".algo-sr h3 a")]
    return links[30:60]

# Function to perform search based on user's choice
def perform_search(query, search_engine_choice, start=0):
    if search_engine_choice == "google":
        return search_google(query, num_results=30)
    elif search_engine_choice == "yahoo":
        return search_yahoo(query, start)

# Load GPT-2 model
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
generate_ia = TextGenerationPipeline(model=model, tokenizer=tokenizer)

# Perform search
search_engine_choice = input("Choose search engine (google, yahoo): ").lower()
query = input("Enter search term: ")
if search_engine_choice == "yahoo":
    query_results = perform_search(query, search_engine_choice, start=30)
else:
    query_results = perform_search(query, search_engine_choice)

# Chat loop
while True:
    try:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chat ended.")
            break

        if user_input.lower() == "results":
            print("Search results:")
            for i, result in enumerate(query_results, start=1):
                print(f"{i}. {result}")
            continue

        if user_input.isdigit() and 1 <= int(user_input) <= len(query_results):
            choice = int(user_input) - 1
            selected_result = query_results[choice]
            print(f"You selected: {selected_result}")

            # Get summary of selected site
            site_summary = get_site_summary(selected_result)
            print(f"Site summary: {site_summary}")

            # Build prompt for AI
            prompt = f"{query} {site_summary[:10]}"

            # Generate AI response
            ia_response = generate_ia(prompt, max_length=50, num_return_sequences=1)[0]["generated_text"]
            print("AI:", ia_response)
        
    except KeyboardInterrupt:
        print("\nChat ended by user.")
        break
