import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z * z + c
    return max_iter

# Configurações do sistema
resolucao = 2000
x_min, x_max = -2.5, 1.5
y_min, y_max = -2, 2
max_iter = 200

# Geração do conjunto de Mandelbrot
imagem = np.zeros((resolucao, resolucao))

for i in range(resolucao):
    for j in range(resolucao):
        x = x_min + (x_max - x_min) * i / resolucao
        y = y_min + (y_max - y_min) * j / resolucao
        c = x + y * 1j
        imagem[j, i] = mandelbrot(c, max_iter)

# Plotagem da imagem
plt.figure(figsize=(10, 10))
plt.imshow(imagem, extent=(x_min, x_max, y_min, y_max), cmap='hot', aspect='auto')
plt.colorbar(label='Número de Iterações')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Conjunto de Mandelbrot')

# Salvar a imagem gerada
plt.savefig('conjunto_mandelbrot.png')

# Exibir a imagem
plt.show()
