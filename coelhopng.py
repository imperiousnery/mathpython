import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
r = 0.5   # taxa de crescimento intrínseca
K = 100   # capacidade de suporte do ambiente
dt = 0.1  # incremento de tempo
t_total = 10  # tempo total da simulação

# Condições iniciais
P0 = 10  # população inicial

# Vetores para armazenar os resultados
t = np.arange(0, t_total, dt)
P = np.zeros_like(t)
P[0] = P0

# Simulação
for i in range(1, len(t)):
    dP_dt = r * P[i-1] * (1 - P[i-1]/K)
    P[i] = P[i-1] + dP_dt * dt

# Plotagem dos resultados
plt.plot(t, P)
plt.xlabel('Tempo')
plt.ylabel('População')
plt.title('Crescimento populacional de coelhos')

# Salvando o gráfico em um arquivo
plt.savefig('grafico_crescimento_coelhos.png')
