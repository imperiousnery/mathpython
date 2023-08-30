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

# Fazer pesquisa no DuckDuckGo
def search_duckduckgo(query):
    search_url = f"https://duckduckgo.com/html/?q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [a['href'] for a in soup.find_all('a', href=True)]
    results = [link for link in links if link.startswith("http")]
    return results

# Fazer pesquisa no mecanismo de busca selecionado em paralelo
def perform_search(query, search_engine_choice):
    if search_engine_choice == "google":
        return search_google(query, num_results=10)
    elif search_engine_choice == "duckduckgo":
        return search_duckduckgo(query)

# Carregar o modelo GPT-2
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
generate_ia = TextGenerationPipeline(model=model, tokenizer=tokenizer)

# Realizar a pesquisa
search_engine_choice = input("Escolha o mecanismo de busca (google, duckduckgo): ").lower()
query = input("Digite o termo de pesquisa: ")
query_results = perform_search(query, search_engine_choice)

# Loop de chat
while True:
    try:
        user_input = input("Você: ")

        if user_input.lower() == "sair":
            print("Chat encerrado.")
            break
        
        # Exibir os resultados de pesquisa
        print("Resultados de pesquisa:")
        for i, result in enumerate(query_results, start=1):
            print(f"{i}. {result}")
        
        choice = input("Escolha um resultado (1-10) ou 'sair': ")
        
        if choice.lower() == "sair":
            print("Chat encerrado.")
            break
        
        choice = int(choice) - 1
        
        # Verificar escolha válida
        if choice < 0 or choice >= len(query_results):
            print("Escolha inválida. Tente novamente.")
            continue
        
        selected_result = query_results[choice]
        
        # Exibir o resultado selecionado
        print("Você escolheu:", selected_result)
        
        # Obter o resumo do conteúdo do site
        content_summary = get_site_summary(selected_result)
        print("IA: Resumo do conteúdo:", content_summary)

        # Montar prompt da IA
        ia_prompt = query + " " + content_summary[:10]  # Usar os primeiros 10 caracteres do resumo
        
        # Gerar resposta com o modelo GPT-2
        ia_response = generate_ia(ia_prompt, max_length=50)[0]["generated_text"]
        print("IA:", ia_response)

    except KeyboardInterrupt:
        print("\nChat encerrado pelo usuário.")
        break
