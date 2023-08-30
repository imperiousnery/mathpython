import requests
from bs4 import BeautifulSoup
from duckduckgo_search import ddg_images
from concurrent.futures import ThreadPoolExecutor
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Função para obter o resumo de um site
def get_site_summary(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")
    text = " ".join(p.get_text() for p in paragraphs)
    return text[:1000]  # Limitar o resumo aos primeiros 1000 caracteres

# Carregar o modelo GPT-2
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Loop de chat
while True:
    try:
        search_engine_choice = input("Escolha o mecanismo de busca (google, duckduckgo, bing, yahoo): ").lower()

        if search_engine_choice not in ["google", "duckduckgo", "bing", "yahoo"]:
            print("Escolha inválida. Tente novamente.")
            continue
        
        user_input = input("Você: ")

        if user_input.lower() == "sair":
            print("Chat encerrado.")
            break
        
        # Fazer pesquisa no mecanismo de busca selecionado em paralelo
        query = user_input
        with ThreadPoolExecutor() as executor:
            if search_engine_choice == "google":
                future = executor.submit(requests.get, f"https://www.google.com/search?q={query}&num=10")
            elif search_engine_choice == "duckduckgo":
                future = executor.submit(ddg_images.search, query, max_results=10)
            elif search_engine_choice == "bing":
                future = executor.submit(requests.get, f"https://www.bing.com/search?q={query}&count=10")
            elif search_engine_choice == "yahoo":
                future = executor.submit(requests.get, f"https://search.yahoo.com/search?p={query}&n=10")
            query_results = future.result()
        
        # Exibir os resultados de pesquisa e permitir que o usuário escolha um
        print("Resultados de pesquisa:")
        if search_engine_choice == "duckduckgo":
            for i, result in enumerate(query_results, start=1):
                print(f"{i}. {result['title']}: {result['url']}")
        else:
            soup = BeautifulSoup(query_results.content, "html.parser")
            for i, result in enumerate(soup.select("a"), start=1):
                print(f"{i}. {result.get_text()}: {result['href']}")
        choice = int(input("Escolha um resultado (1-10): ")) - 1
        
        # Verificar escolha válida
        if choice < 0 or choice >= 10:
            print("Escolha inválida. Tente novamente.")
            continue
        
        selected_result = query_results[choice]
        
        # Obter o resumo do conteúdo do site
        content_summary = get_site_summary(selected_result)
        print("IA: Resumo do conteúdo:", content_summary)

        # Montar prompt da IA
        ia_prompt = query + " " + content_summary[:100]  # Usar os primeiros 100 caracteres do resumo
        
        # Gerar resposta com o modelo GPT-2
        ia_response = generate_ia_response(ia_prompt)
        print("IA:", ia_response)

    except KeyboardInterrupt:
        print("\nChat encerrado pelo usuário.")
        break
