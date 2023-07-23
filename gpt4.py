# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Função F(x) com os coeficientes ajustados previamente
def F(x, a_fit, b_fit):
    return a_fit * x + b_fit

# Função G(y) com os coeficientes ajustados previamente (suponha que eles já foram obtidos)
def G(y):
    # Suponha que os coeficientes b0, b1, b2, ..., bm foram obtidos previamente por dados reais dos zeros não triviais
    b0 = 0.5
    b1 = -0.2
    b2 = 0.1
    # Adicione mais coeficientes b conforme necessário, dependendo do grau do polinômio desejado

    # Função polinomial G(y)
    return b0 + b1 * y + b2 * y**2

# Valores de x e y para a simulação
start_y = -10
end_y = 10
random_y_values = [random.uniform(start_y, end_y) for _ in range(5)]

# Função F(x) ajustada
a_fit = 0.7
b_fit = 0.3

# Plot dos dados simulados e função F(x) ajustada
plt.scatter(yi_data, Gi_data, label='Dados simulados')
x_fit = np.linspace(start_y, end_y, 100)
plt.plot(x_fit, F(x_fit, a_fit, b_fit), 'r', label='F(x) ajustada')

# Plot da função G(y) ajustada
y_fit = np.linspace(start_y, end_y, 100)
plt.plot(y_fit, G(y_fit), 'g', label='G(y) ajustada')

# Mostrar o gráfico
plt.xlabel('Parte Imaginária (y)')
plt.ylabel('Parte Real (Gi)')
plt.legend()
plt.grid(True)
plt.title('Ajuste de Curvas para as funções F(x) e G(y)')

# Salvar a imagem
plt.savefig('ajuste_de_curvas.png')  # Altere o nome do arquivo e a extensão conforme necessário

# Mostrar o gráfico
plt.show()
