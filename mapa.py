import numpy as np
import matplotlib.pyplot as plt

def mapa_logistico(x0, r, num_iteracoes):
    # Vetor para armazenar os valores do mapa logístico
    valores = np.zeros(num_iteracoes)

    # Condição inicial
    valores[0] = x0

    # Iterações do mapa logístico
    for i in range(1, num_iteracoes):
        valores[i] = r * valores[i-1] * (1 - valores[i-1])

    return valores

# Parâmetros do sistema
x0 = 0.2  # Condição inicial
num_iteracoes = 1000  # Número de iterações

# Valores de r para simulação
valores_r = np.linspace(2.5, 4.0, 500)

# Simulação para cada valor de r
for r in valores_r:
    valores_mapa = mapa_logistico(x0, r, num_iteracoes)
    plt.plot([r] * num_iteracoes, valores_mapa, ',k', alpha=0.01)

# Configurações do gráfico
plt.xlabel('Valor de r')
plt.ylabel('Valores do mapa logístico')
plt.title('Diagrama de Bifurcação')
plt.show()
plt.savefig('diagrama_bifurcacao.png')
