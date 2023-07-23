import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Função "G(y)" que queremos ajustar com base nos dados dos zeros não triviais
def G(y, *coeffs):
    result = 0
    for i, coeff in enumerate(coeffs):
        result += coeff * (y ** i)
    return result

# Função para verificar se um número é primo
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Dados hipotéticos dos zeros não triviais da função zeta de Riemann
np.random.seed(42)  # Definir a semente do gerador de números aleatórios para reprodutibilidade
n = 100  # Número de dados hipotéticos a serem gerados
y_data = np.sort(np.random.uniform(0, 10, n))  # Parte imaginária dos zeros não triviais (valores aleatórios entre 0 e 10)
real_coeffs = [2.5, 0.5, -1.2, 0.8]  # Coeficientes reais do polinômio G(y) que usamos para gerar os dados
G_data = G(y_data, *real_coeffs) + np.random.normal(0, 0.5, n)  # Valores reais associados aos zeros não triviais (com ruído gaussiano)

# Identificar quais valores da parte imaginária são primos
primes = [y for y in y_data if is_prime(int(y))]

# Função objetivo a ser minimizada (soma dos quadrados das diferenças)
def objective_function(coeffs, y_data, G_data):
    predicted_G = G(y_data, *coeffs)
    return np.sum((G_data - predicted_G) ** 2)

# Chute inicial para os coeficientes "b0, b1, b2, ..., bm"
m = 3  # Grau do polinômio para representar a função "G(y)"
initial_coeffs_guess = np.ones(m + 1)

# Otimização usando o método dos mínimos quadrados
result = minimize(objective_function, initial_coeffs_guess, args=(y_data, G_data))

# Coeficientes ajustados
adjusted_coeffs = result.x

# Plotar a função "G(y)" ajustada junto com os dados hipotéticos e os números primos
y_values = np.linspace(0, 10, 1000)
G_values_adjusted = G(y_values, *adjusted_coeffs)

plt.scatter(y_data, G_data, label='Dados Hipotéticos')
plt.plot(y_values, G_values_adjusted, color='red', label='G(y) Ajustado')
plt.scatter(primes, G(np.array(primes), *adjusted_coeffs), color='green', marker='o', s=100, label='Números Primos')
plt.xlabel('y (Parte Imaginária)')
plt.ylabel('G(y)')
plt.legend()
plt.title('Ajuste da função G(y) usando o Método dos Mínimos Quadrados')

# Salvar o gráfico em uma imagem
plt.savefig('ajuste_G(y)_com_primos.png')

plt.show()

print("Coeficientes reais:", real_coeffs)
print("Coeficientes ajustados:", adjusted_coeffs)
