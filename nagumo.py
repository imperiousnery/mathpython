import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
epsilon = 0.08
a = 0.7
b = 0.8
I = 0.5
dt = 0.01
t_total = 100.0

# Condições iniciais
V0 = -1.0
W0 = -0.5

# Vetores para armazenar os resultados
t = np.arange(0, t_total, dt)
V = np.zeros_like(t)
W = np.zeros_like(t)
V[0] = V0
W[0] = W0

# Simulação
for i in range(1, len(t)):
    dV_dt = V[i-1] - (V[i-1]**3)/3 - W[i-1] + I
    dW_dt = epsilon * (V[i-1] + a - b * W[i-1])
    V[i] = V[i-1] + dV_dt * dt
    W[i] = W[i-1] + dW_dt * dt

# Plotagem dos resultados
plt.plot(t, V, label='Potencial de membrana')
plt.plot(t, W, label='Variável de recuperação')
plt.xlabel('Tempo')
plt.ylabel('Valor')
plt.title('Sistema de FitzHugh-Nagumo')
plt.legend()

# Salvando o gráfico em uma imagem
plt.savefig('grafico_fitzhugh_nagumo.png')
