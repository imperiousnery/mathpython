from googlesearch import search
import random
import re
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Função para gerar uma frase de 5 palavras baseada no conteúdo
def generate_phrase(content):
    words = re.findall(r'\w+', content)
    selected_words = random.sample(words, min(5, len(words)))
    return ' '.join(selected_words)

# Carregar o modelo GPT-2
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Loop de chat
while True:
    try:
        user_input = input("Você: ")

        if user_input.lower() == "sair":
            print("Chat encerrado.")
            break
        
        # Fazer pesquisa no Google
        query = user_input
        query_results = search(query, num_results=10)  # Exibir 10 resultados
        
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

        # Gerar frase de 5 palavras baseada no conteúdo escolhido
        content = selected_result.split(" - ")[0]  # Extrair conteúdo antes do hífen
        phrase = generate_phrase(content)
        
        print("IA: Frase gerada:", phrase)

        # Gerar resposta adicional com o modelo GPT-2
        prompt = "IA: " + phrase + "\nVocê:"
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        print("IA:", generated_text)

    except KeyboardInterrupt:
        print("\nChat encerrado pelo usuário.")
        break
