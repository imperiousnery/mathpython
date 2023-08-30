import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Carregar o modelo e o tokenizador do distilGPT-2
model_name = "distilgpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Texto de entrada para gerar continuação
input_text = "Uma vez upon a time"

# Codificar o texto de entrada para IDs numéricos
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Gerar texto continuado com máscara de atenção
output = model.generate(input_ids, max_length=50, num_return_sequences=1, attention_mask=input_ids)

# Decodificar IDs numéricos para texto
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
