import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parâmetros
m1 = 1.0  # massa do pêndulo 1
m2 = 1.0  # massa do pêndulo 2
L1 = 1.0  # comprimento da haste do pêndulo 1
L2 = 1.0  # comprimento da haste do pêndulo 2
g = 9.81  # aceleração da gravidade

# Condições iniciais
theta1_0 = np.pi / 2  # posição angular inicial do pêndulo 1
theta2_0 = np.pi / 2  # posição angular inicial do pêndulo 2
theta1_dot_0 = 0.0    # velocidade angular inicial do pêndulo 1
theta2_dot_0 = 0.0    # velocidade angular inicial do pêndulo 2

# Função que retorna as derivadas das variáveis em relação ao tempo
def pendulum_dynamics(t, y):
    theta1, theta2, theta1_dot, theta2_dot = y

    theta1_double_dot = (m2 * L1 * theta1_dot**2 * np.sin(theta2 - theta1) * np.cos(theta2 - theta1) +
                         m2 * g * np.sin(theta2) * np.cos(theta2 - theta1) +
                         m2 * L2 * theta2_dot**2 * np.sin(theta2 - theta1) -
                         (m1 + m2) * g * np.sin(theta1)) / (L1 * (m1 + m2 * np.sin(theta2 - theta1)**2))

    theta2_double_dot = ((m1 + m2) * L1 * theta1_dot**2 * np.sin(theta2 - theta1) * np.cos(theta2 - theta1) +
                         (m1 + m2) * g * np.sin(theta1) * np.cos(theta2 - theta1) -
                         (m1 + m2) * L2 * theta2_dot**2 * np.sin(theta2 - theta1) -
                         (m1 + m2) * g * np.sin(theta2)) / (L2 * (m1 + m2 * np.sin(theta2 - theta1)**2))

    return [theta1_dot, theta2_dot, theta1_double_dot, theta2_double_dot]

# Tempo de simulação
t_start = 0.0
t_end = 10.0
dt = 0.01
t = np.arange(t_start, t_end, dt)

# Condições iniciais como vetor
y0 = [theta1_0, theta2_0, theta1_dot_0, theta2_dot_0]

# Solução numérica das equações diferenciais
sol = solve_ivp(pendulum_dynamics, [t_start, t_end], y0, t_eval=t)

# Plotagem dos resultados
plt.plot(sol.t, sol.y[0], label='Pêndulo 1')
plt.plot(sol.t, sol.y[1], label='Pêndulo 2')
plt.xlabel('Tempo')
plt.ylabel('Ângulo (rad)')
plt.title('Pêndulo Duplo')
plt.legend()

# Salvando o gráfico em uma imagem
plt.savefig('grafico_pendulo_duplo.png')
