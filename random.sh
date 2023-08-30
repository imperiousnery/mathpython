#!/bin/bash

src_dir="./"
math_keywords=("algebra" "calculus" "geometry" "statistics" "trigonometry")

for py_file in "$src_dir"*.py; do
    base_name=$(basename "$py_file" .py)
    
    # Obtém a primeira linha que contém um import
    first_import=$(grep -m 1 -E '^import |^from ' "$py_file")
    
    # Extrai o nome do módulo/import da linha
    module_name=$(echo "$first_import" | awk '{print $2}')
    
    # Obtém a data de criação do arquivo
    create_date=$(stat -c %Y "$py_file")
    formatted_date=$(date -d "@$create_date" "+%Y%m%d")
    
    # Seleciona uma palavra-chave aleatoriamente
    random_keyword=${math_keywords[$RANDOM % ${#math_keywords[@]}]}
    
    # Novo nome para o arquivo
    new_name="${formatted_date}_${module_name}_${random_keyword}.py"
    
    # Move o arquivo para o novo nome
    mv "$py_file" "$src_dir$new_name"
done

echo "Arquivos renomeados e organizados com base nas importações, na data de criação e com uma palavra aleatória!"
