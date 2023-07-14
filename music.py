import numpy as np
import matplotlib.pyplot as plt

# Dados das notas musicais
notas = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
frequencias = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]

# Criação do gráfico
fig, ax = plt.subplots()
ax.set_xlabel('Nota')
ax.set_ylabel('Frequência (Hz)')
ax.set_title('Organização de Notas Musicais')

# Plotagem das notas no gráfico
ax.scatter(notas, frequencias, color='blue')

# Salvando o gráfico em uma imagem
plt.savefig('grafico_notas_musicais.png')

# Exibição do gráfico
plt.show()
