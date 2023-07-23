import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sympy import primerange

# Restante do código aqui...

# Plot dos dados simulados
plt.scatter(yi_data, Gi_data, label='Dados simulados')

# Plot da função F(x) ajustada
x_fit = np.linspace(start_y, end_y, 100)
plt.plot(x_fit, F(x_fit, a_fit, b_fit), 'r', label='F(x) ajustada')

# Plot da função G(y) ajustada
y_fit = np.linspace(start_y, end_y, 100)
plt.plot(y_fit, G(y_fit, b0_fit, b1_fit), 'g', label='G(y) ajustada')

# Plot do número complexo z e o valor M(z) encontrado
z = complex(2, 0.3)
plt.scatter(z.imag, F(z.real, a_fit, b_fit) + G(z.imag, b0_fit, b1_fit), color='orange', label='M(z)')

plt.xlabel('Parte Imaginária (y)')
plt.ylabel('Parte Real (Gi)')
plt.legend()
plt.grid(True)
plt.title('Ajuste de Curvas para a função M(z)')

# Salvar a imagem
plt.savefig('ajuste_de_curvas.png')  # Altere o nome do arquivo e a extensão conforme necessário

# Mostrar o gráfico
plt.show()
