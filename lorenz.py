import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parâmetros
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0
dt = 0.01
t_total = 50.0

# Condições iniciais
x0 = 1.0
y0 = 1.0
z0 = 1.0

# Vetores para armazenar os resultados
t = np.arange(0, t_total, dt)
x = np.zeros_like(t)
y = np.zeros_like(t)
z = np.zeros_like(t)
x[0] = x0
y[0] = y0
z[0] = z0

# Simulação
for i in range(1, len(t)):
    dx_dt = sigma * (y[i-1] - x[i-1])
    dy_dt = x[i-1] * (rho - z[i-1]) - y[i-1]
    dz_dt = x[i-1] * y[i-1] - beta * z[i-1]
    x[i] = x[i-1] + dx_dt * dt
    y[i] = y[i-1] + dy_dt * dt
    z[i] = z[i-1] + dz_dt * dt

# Plotagem dos resultados
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Sistema de Lorenz')

# Salvando o gráfico em uma imagem
plt.savefig('grafico_lorenz.png')
