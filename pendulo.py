import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
g = 9.81  # aceleração da gravidade (m/s^2)
L = 1.0   # comprimento da haste (metros)
dt = 0.01  # incremento de tempo
t_total = 10.0  # tempo total da simulação

# Condições iniciais
theta0 = np.pi / 4  # posição angular inicial (rad)
theta_dot0 = 0.0    # velocidade angular inicial (rad/s)

# Vetores para armazenar os resultados
t = np.arange(0, t_total, dt)
theta = np.zeros_like(t)
theta_dot = np.zeros_like(t)
theta[0] = theta0
theta_dot[0] = theta_dot0

# Simulação
for i in range(1, len(t)):
    theta_double_dot = -(g / L) * np.sin(theta[i-1])
    theta_dot[i] = theta_dot[i-1] + theta_double_dot * dt
    theta[i] = theta[i-1] + theta_dot[i] * dt

# Plotagem dos resultados
plt.plot(t, theta)
plt.xlabel('Tempo')
plt.ylabel('Ângulo (rad)')
plt.title('Oscilação de um pêndulo simples')

# Salvando o gráfico em uma imagem
plt.savefig('grafico_pendulo_simples.png')
