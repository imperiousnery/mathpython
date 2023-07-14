import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
N = 100  # número de osciladores
K = 1.0  # parâmetro de acoplamento
omega_mean = 2.0  # frequência média dos osciladores
sigma = 0.5  # desvio padrão das frequências dos osciladores
dt = 0.01  # incremento de tempo
t_total = 10.0  # tempo total da simulação

# Frequências dos osciladores
omega = np.random.normal(omega_mean, sigma, N)

# Condições iniciais
theta = np.random.uniform(0, 2*np.pi, N)  # fases iniciais

# Vetor para armazenar os resultados
t = np.arange(0, t_total, dt)
phases = np.zeros((len(t), N))
phases[0] = theta

# Simulação
for i in range(1, len(t)):
    delta_theta = omega + (K/N) * np.sum(np.sin(phases[i-1] - phases[i-1][:, np.newaxis]), axis=1)
    phases[i] = phases[i-1] + delta_theta * dt

# Plotagem dos resultados
for i in range(N):
    plt.plot(t, phases[:, i])

plt.xlabel('Tempo')
plt.ylabel('Fase')
plt.title('Modelo de Kuramoto - Osciladores acoplados')

# Salvando o gráfico em uma imagem
plt.savefig('grafico_osciladores_acoplados.png')
