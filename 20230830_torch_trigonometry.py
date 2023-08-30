import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Nome do modelo
model_name = "distilgpt2"

# Carregar o modelo e o tokenizador do distilGPT-2
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

while True:
    try:
        # Receber entrada do usuário
        user_input = input("Você: ")

        # Encerrar o loop se o usuário digitar "sair"
        if user_input.lower() == "sair":
            print("Chat encerrado.")
            break

        # Codificar a entrada do usuário para IDs numéricos
        input_ids = tokenizer.encode(user_input, return_tensors="pt")

        # Gerar resposta
        output = model.generate(input_ids, max_length=100, num_return_sequences=1)

        # Decodificar IDs numéricos para texto
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        print("IA:", generated_text)
        
    except KeyboardInterrupt:
        print("\nChat encerrado pelo usuário.")
        break
