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

# Função para analisar o padrão de distância entre números primos para um determinado tamanho de conjunto
def analyze_prime_distances(n):
    # Dados hipotéticos dos zeros não triviais da função zeta de Riemann
    np.random.seed(42)  # Definir a semente do gerador de números aleatórios para reprodutibilidade
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

    # Calcular as diferenças entre os valores da parte imaginária correspondentes aos números primos
    prime_diffs = np.diff(np.array(primes))

    # Exibir o resultado
    print(f"\nAnálise para {n} números:")
    print("Coeficientes reais:", real_coeffs)
    print("Coeficientes ajustados:", adjusted_coeffs)
    print("Diferenças entre números primos:", prime_diffs)

# Análise para diferentes tamanhos de conjuntos
analyze_prime_distances(100)
analyze_prime_distances(1000)
analyze_prime_distances(10000)
