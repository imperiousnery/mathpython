import requests
from bs4 import BeautifulSoup
from googlesearch import search
from concurrent.futures import ThreadPoolExecutor
import time
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextGenerationPipeline

# Função para obter o resumo de um site
def get_site_summary(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")
    text = " ".join(p.get_text() for p in paragraphs)
    return text[:1000]  # Limitar o resumo aos primeiros 1000 caracteres

# Fazer pesquisa no Google com intervalos
def search_google(query, num_results):
    results = []
    for result in search(query, num_results=num_results):
        results.append(result)
        time.sleep(1)  # Intervalo de 1 segundo entre as solicitações
    return results

# Fazer pesquisa no Yahoo diretamente via URL
def search_yahoo(query, start):
    url = f"https://search.yahoo.com/search?p={query}&b={start}&n=30"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [a['href'] for a in soup.select(".algo-sr h3 a")]
    return links

# Fazer pesquisa no mecanismo de busca selecionado em paralelo
def perform_search(query, search_engine_choice, start=0):
    if search_engine_choice == "google":
        return search_google(query, num_results=30)
    elif search_engine_choice == "yahoo":
        return search_yahoo(query, start)

# Carregar o modelo GPT-2
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
generate_ia = TextGenerationPipeline(model=model, tokenizer=tokenizer)

# Realizar a pesquisa
search_engine_choice = input("Escolha o mecanismo de busca (google, yahoo): ").lower()
query = input("Digite o termo de pesquisa: ")
query_results = perform_search(query, search_engine_choice)

# Loop de chat
while True:
    try:
        user_input = input("Você: ")

        if user_input.lower() == "sair":
            print("Chat encerrado.")
            break

        if user_input.lower() == "resultados":
            print("Resultados de pesquisa:")
            for i, result in enumerate(query_results, start=1):
                print(f"{i}. {result}")
            continue

        if user_input.isdigit() and 1 <= int(user_input) <= 30:
            choice = int(user_input) - 1
            selected_result = query_results[choice]
            print(f"Você selecionou o resultado: {selected_result}")

            # Obter o resumo do site selecionado
            site_summary = get_site_summary(selected_result)
            print(f"Resumo do site: {site_summary}")

            # Construir o prompt para a IA
            prompt = f"{query} {site_summary[:10]}"

            # Gerar resposta da IA
            ia_response = generate_ia(prompt, max_length=50, num_return_sequences=1)[0]["generated_text"]
            print("IA:", ia_response)
        
    except KeyboardInterrupt:
        print("\nChat encerrado pelo usuário.")
        break
