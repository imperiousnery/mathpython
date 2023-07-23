import numpy as np
from sympy import primerange

# Função F(x) = ax + b (Exemplo de função polinomial para a parte real)
def F(x, a, b):
    return a * x + b

# Função G(y) = b0 + b1y (Exemplo de função polinomial para a parte imaginária)
def G(y, b0, b1):
    return b0 + b1 * y

# Função para verificar se um número é primo
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Dados simulados dos zeros não triviais da função zeta de Riemann
# Vamos gerar números primos complexos simulados para a parte imaginária (y) dos zeros não triviais
# Aqui, definimos um intervalo arbitrário para a parte imaginária dos números primos
start_y = 0.1
end_y = 0.5

# Gerando números primos complexos no intervalo especificado
yi_data = np.array(list(primerange(int(start_y*10), int(end_y*10)+1))) / 10

# Valores simulados para a parte real dos zeros não triviais (dados hipotéticos)
Gi_data = np.array([1.0, 2.0, 3.0])  # Valores reais associados aos zeros não triviais

# Ajuste dos coeficientes da função F(x) e G(y) usando o método dos mínimos quadrados
popt_f = np.polyfit(yi_data, Gi_data, deg=1)
popt_g = np.polyfit(yi_data, Gi_data, deg=1)

# Obtendo os coeficientes ajustados da função F(x)
a_fit, b_fit = popt_f

# Obtendo os coeficientes ajustados da função G(y)
b0_fit, b1_fit = popt_g

# Exemplo de uso com o número complexo z = x + yi
z = complex(2, 0.3)

# Calculando M(z) para o número complexo dado usando os coeficientes ajustados
real_part = F(z.real, a_fit, b_fit)
imag_part = G(z.imag, b0_fit, b1_fit)

print("Número complexo simulado:", z)
print("Parte Real:", real_part)
print("Parte Imaginária:", imag_part)

# Verificando se a parte imaginária é um número primo
if is_prime(int(imag_part)):
    print("A parte imaginária é um número primo.")
else:
    print("A parte imaginária NÃO é um número primo.")
