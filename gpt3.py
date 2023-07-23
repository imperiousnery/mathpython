# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sympy import primerange
import random

# Função F(x) = ax + b (Exemplo de função polinomial para a parte real)
def F(x, a, b):
    return a * x + b

# Função G(y) = b0 + b1y (Exemplo de função polinomial para a parte imaginária)
def G(y, b0, b1):
    return b0 + b1 * y

# Dados simulados dos zeros não triviais da função zeta de Riemann
# Vamos gerar números primos complexos simulados para a parte imaginária (y) dos zeros não triviais
# Aqui, definimos um intervalo arbitrário para a parte imaginária dos números primos
start_y = 0.1
end_y = 0.5

# Gerando números primos complexos no intervalo especificado
yi_data = np.array(list(primerange(int(start_y*10), int(end_y*10)+1))) / 10

# Valores simulados para a parte real dos zeros não triviais (dados hipotéticos)
Gi_data = np.array([1.0, 2.0, 3.0])  # Valores reais associados aos zeros não triviais

# Realizando o ajuste dos coeficientes da função F(x) usando o método dos mínimos quadrados
popt_f, _ = curve_fit(F, yi_data, Gi_data)

# Obtendo os coeficientes ajustados da função F(x)
a_fit, b_fit = popt_f

# Realizando o ajuste dos coeficientes da função G(y) usando o método dos mínimos quadrados
popt_g, _ = curve_fit(G, yi_data, Gi_data)

# Obtendo os coeficientes ajustados da função G(y)
b0_fit, b1_fit = popt_g

# Gera 5 valores aleatórios para a parte imaginária (y) de z
random_y_values = [random.uniform(start_y, end_y) for _ in range(5)]

# Calcula e mostra os 5 valores de M(z) com base nos valores aleatórios de y
print("Valores de M(z) para 5 números complexos aleatórios:")
for y in random_y_values:
    z = complex(random.uniform(-10, 10), y)
    m_z = F(z.real, a_fit, b_fit) + G(z.imag, b0_fit, b1_fit)
    print(f"M({z}) =", m_z)

# Plot dos dados simulados
plt.scatter(yi_data, Gi_data, label='Dados simulados')

# Plot da função F(x) ajustada
x_fit = np.linspace(start_y, end_y, 100)
plt.plot(x_fit, F(x_fit, a_fit, b_fit), 'r', label='F(x) ajustada')

# Plot da função G(y) ajustada
y_fit = np.linspace(start_y, end_y, 100)
plt.plot(y_fit, G(y_fit, b0_fit, b1_fit), 'g', label='G(y) ajustada')

# Plot do número complexo z e o valor M(z) encontrado
plt.scatter([z.imag for z in random_y_values], [F(z.real, a_fit, b_fit) + G(z.imag, b0_fit, b1_fit) for z in random_y_values], color='orange', label='M(z)')

plt.xlabel('Parte Imaginária (y)')
plt.ylabel('Parte Real (Gi)')
plt.legend()
plt.grid(True)
plt.title('Ajuste de Curvas para a função M(z)')

# Salvar a imagem
plt.savefig('ajuste_de_curvas.png')  # Altere o nome do arquivo e a extensão conforme necessário

# Mostrar o gráfico
plt.show()
