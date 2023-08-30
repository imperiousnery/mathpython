import torch
from transformers import DistilGPT2Tokenizer, DistilGPT2Model

# Carregar o modelo e o tokenizador do distilGPT-2
model_name = "distilgpt2"
model = DistilGPT2Model.from_pretrained(model_name)
tokenizer = DistilGPT2Tokenizer.from_pretrained(model_name)

# Texto de entrada para gerar continuação
input_text = "Uma vez upon a time"

# Codificar o texto de entrada para IDs numéricos
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Gerar texto continuado
output = model.generate(input_ids, max_length=50, num_return_sequences=1)

# Decodificar IDs numéricos para texto
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
