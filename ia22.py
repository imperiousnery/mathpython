import requests
from bs4 import BeautifulSoup
from duckduckgo_search import ddg
from googlesearch import search
from concurrent.futures import ThreadPoolExecutor
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextGenerationPipeline

# Função para gerar a resposta da IA
def generate_ia_response(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(output[0], skip_special_tokens=True)

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
generate_ia = TextGenerationPipeline(model=model, tokenizer=tokenizer)

# Loop de chat
while True:
    try:
        search_engine_choice = input("Escolha o mecanismo de busca (google, duckduckgo): ").lower()

        if search_engine_choice not in ["google", "duckduckgo"]:
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
                future = executor.submit(search, query, num=10, stop=10)
            elif search_engine_choice == "duckduckgo":
                future = executor.submit(ddg.search, query, max_results=10)
            query_results = future.result()
        
        # Exibir os resultados de pesquisa e permitir que o usuário escolha um
        print("Resultados de pesquisa:")
        for i, result in enumerate(query_results, start=1):
            print(f"{i}. {result}")
        choice = int(input("Escolha um resultado (1-10): ")) - 1
        
        # Verificar escolha válida
        if choice < 0 or choice >= len(query_results):
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
