from googlesearch import search
import random
import re
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Função para gerar resumo baseado nos resultados da pesquisa
def generate_summary(query_results):
    relevant_results = list(query_results)
    if not relevant_results:
        return "Desculpe, não encontrei informações relevantes."
    return random.choice(relevant_results)

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
        query_results = search(query, num_results=5)  # Limitar a 5 resultados

        # Gerar resumo baseado nos resultados da pesquisa
        summary = generate_summary(query_results)
        print("IA:", summary)

        # Gerar resposta adicional com o modelo GPT-2
        prompt = "IA: " + summary + "\nVocê:"
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        print("IA:", generated_text)

    except KeyboardInterrupt:
        print("\nChat encerrado pelo usuário.")
        break
