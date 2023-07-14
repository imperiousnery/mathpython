import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
a = 0.5   # taxa de crescimento dos coelhos
b = 0.1   # taxa de predação dos lobos
c = 0.05  # eficiência de conversão dos lobos
d = 0.2   # taxa de mortalidade dos lobos
dt = 0.01  # incremento de tempo
t_total = 50.0  # tempo total da simulação

# Condições iniciais
R0 = 100  # população inicial de coelhos
L0 = 50   # população inicial de lobos

# Vetores para armazenar os resultados
t = np.arange(0, t_total, dt)
R = np.zeros_like(t)
L = np.zeros_like(t)
R[0] = R0
L[0] = L0

# Simulação
for i in range(1, len(t)):
    dR_dt = a * R[i-1] - b * R[i-1] * L[i-1]
    dL_dt = c * b * R[i-1] * L[i-1] - d * L[i-1]
    R[i] = R[i-1] + dR_dt * dt
    L[i] = L[i-1] + dL_dt * dt

# Plotagem dos resultados
plt.plot(t, R, label='Coelhos')
plt.plot(t, L, label='Lobos')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.title('Dinâmica de predador-presa')
plt.legend()

# Salvando o gráfico em uma imagem
plt.savefig('grafico_predador_presa.png')
