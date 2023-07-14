import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
total_notas = 12  # Total de notas musicais
total_acordes = 8  # Total de acordes na progressão
tempo_total = 5.0  # Tempo total da simulação em segundos
dt = 0.01  # Passo de tempo
num_pontos = int(tempo_total / dt)  # Número de pontos da simulação

# Distribuição inicial de probabilidades dos acordes
prob_acordes_inicial = np.array([0.1, 0.2, 0.1, 0.1, 0.15, 0.1, 0.15, 0.1])

# Distribuição inicial de notas para cada acorde
prob_notas_inicial = np.array([[0.2, 0.15, 0.1, 0.05, 0.1, 0.1, 0.15, 0.05, 0.0, 0.05, 0.0, 0.0],
                               [0.1, 0.15, 0.05, 0.2, 0.05, 0.05, 0.2, 0.0, 0.0, 0.05, 0.05, 0.0],
                               [0.0, 0.05, 0.1, 0.15, 0.05, 0.1, 0.15, 0.05, 0.0, 0.15, 0.05, 0.0],
                               [0.05, 0.05, 0.2, 0.15, 0.05, 0.05, 0.15, 0.0, 0.05, 0.1, 0.0, 0.05],
                               [0.1, 0.1, 0.1, 0.1, 0.05, 0.1, 0.1, 0.05, 0.0, 0.1, 0.0, 0.1],
                               [0.05, 0.05, 0.05, 0.05, 0.2, 0.1, 0.1, 0.1, 0.0, 0.2, 0.0, 0.05],
                               [0.0, 0.0, 0.05, 0.1, 0.05, 0.1, 0.2, 0.1, 0.0, 0.3, 0.0, 0.0],
                               [0.15, 0.15, 0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.05, 0.05, 0.05, 0.05]])

# Geração da progressão de acordes ao longo do tempo
progressao_acordes = np.zeros((num_pontos, total_acordes))
progressao_acordes[0] = prob_acordes_inicial

for i in range(1, num_pontos):
    progressao_acordes[i] = progressao_acordes[i-1]

# Geração das notas musicais para cada acorde
notas_acordes = np.zeros((num_pontos, total_acordes, total_notas))
notas_acordes[0] = prob_notas_inicial

for i in range(1, num_pontos):
    for j in range(total_acordes):
        notas_acordes[i][j] = notas_acordes[i-1][j]

# Simulação
for i in range(1, num_pontos):
    for j in range(total_acordes):
        notas_acordes[i][j] = notas_acordes[i][j] / np.sum(notas_acordes[i][j])  # Normalização das probabilidades das notas
        progressao_acordes[i][j] = np.dot(progressao_acordes[i-1], notas_acordes[i-1][:, j])  # Atualização da progressão

# Plotagem dos resultados
tempos = np.linspace(0, tempo_total, num_pontos)

fig, ax = plt.subplots(nrows=total_acordes+1, figsize=(8, 10), sharex=True)

for i in range(total_acordes):
    ax[i].plot(tempos, progressao_acordes[:, i])
    ax[i].set_ylabel(f'Acorde {i+1}')

ax[total_acordes].set_xlabel('Tempo (s)')
ax[total_acordes].set_ylabel('Probabilidade')
ax[total_acordes].set_title('Progressão de Acordes')

plt.tight_layout()
plt.savefig('grafico_progressao_acordes.png')
plt.show()
