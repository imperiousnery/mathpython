from googlesearch import search
import requests
from bs4 import BeautifulSoup
import random
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Carregar o modelo GPT-2
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Função para obter o resumo de um site
def get_site_summary(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")
    text = " ".join(p.get_text() for p in paragraphs)
    return text[:1000]  # Limitar o resumo aos primeiros 1000 caracteres

# Loop de chat
previous_responses = set()  # Armazenar respostas anteriores para evitar repetições
while True:
    try:
        user_input = input("Você: ")

        if user_input.lower() == "sair":
            print("Chat encerrado.")
            break
        
        # Fazer pesquisa no Google
        query = user_input
        query_results = list(search(query, num_results=10))  # Converter para lista
        
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

        # Gerar frase de 5 palavras baseada no resumo do conteúdo
        words = content_summary.split()
        first_phrase = " ".join(words[:5])

        # Montar prompt da IA
        ia_prompt = query + " " + first_phrase
        
        # Evitar repetição de respostas
        if ia_prompt in previous_responses:
            print("IA: Já respondi a isso. Tente outra pergunta.")
            continue
        previous_responses.add(ia_prompt)
        
        # Gerar resposta adicional com o modelo GPT-2
        input_ids = tokenizer.encode("IA: " + ia_prompt + "\nVocê:", return_tensors="pt")
        output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        print("IA:", generated_text)

    except KeyboardInterrupt:
        print("\nChat encerrado pelo usuário.")
        break
