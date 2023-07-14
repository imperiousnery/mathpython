import numpy as np
import matplotlib.pyplot as plt

def chua_system(x, y, z, alpha, beta, m0, m1, m2):
    dx_dt = alpha * (y - x - m0 * f_chua(x))
    dy_dt = x - y + z
    dz_dt = -beta * y
    return dx_dt, dy_dt, dz_dt

def f_chua(x):
    if x < -1:
        return m1 * x + 0.5 * (m0 - m1) * (-1 + np.sqrt(1 + 4 / m1))
    elif x < 1:
        return m0 * x
    else:
        return m1 * x + 0.5 * (m0 - m1) * (1 + np.sqrt(1 - 4 / m1))

# Parâmetros do sistema
alpha = 15.6
beta = 28.0
m0 = -1.143
m1 = -0.714
m2 = -0.143

# Condições iniciais
x0 = 0.1
y0 = 0.1
z0 = 0.1

# Parâmetros de simulação
dt = 0.01  # Passo de tempo
num_steps = 10000  # Número de passos de simulação

# Vetores para armazenar as coordenadas do sistema de Chua
x_values = np.zeros(num_steps)
y_values = np.zeros(num_steps)
z_values = np.zeros(num_steps)

# Simulação do sistema de Chua
x = x0
y = y0
z = z0

for i in range(num_steps):
    x_values[i] = x
    y_values[i] = y
    z_values[i] = z

    dx_dt, dy_dt, dz_dt = chua_system(x, y, z, alpha, beta, m0, m1, m2)
    x += dx_dt * dt
    y += dy_dt * dt
    z += dz_dt * dt

# Plotagem do sistema de Chua
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_values, y_values, z_values)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Sistema de Chua')

# Salvar a imagem do sistema de Chua
plt.savefig('sistema_chua.png')

plt.show()
