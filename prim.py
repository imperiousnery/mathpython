import numpy as np
from scipy.optimize import curve_fit

# Função F(x) = ax^2 + bx + c (Exemplo de função polinomial para a parte real)
def F(x, a, b, c):
    return a * x**2 + b * x + c

# Função G(y) = b0 + b1y + b2y^2 + b3y^3 (Exemplo de função polinomial para a parte imaginária)
def G(y, b0, b1, b2, b3):
    return b0 + b1 * y + b2 * y**2 + b3 * y**3

# Dados simulados dos zeros não triviais da função zeta de Riemann
# Vamos gerar números primos complexos simulados para a parte imaginária (y) dos zeros não triviais
# Aqui, definimos um intervalo arbitrário para a parte imaginária dos números primos
start_y = 0.1
end_y = 0.5

# Gerando números primos complexos no intervalo especificado
yi_data = np.array(list(primerange(int(start_y*10), int(end_y*10)+1))) / 10

# Valores simulados para a parte real dos zeros não triviais (dados hipotéticos)
Gi_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])  # Valores reais associados aos zeros não triviais

# Realizando o ajuste dos coeficientes da função F(x) usando o método dos mínimos quadrados
popt_f, _ = curve_fit(F, yi_data, Gi_data)

# Obtendo os coeficientes ajustados da função F(x)
a_fit, b_fit, c_fit = popt_f

# Realizando o ajuste dos coeficientes da função G(y) usando o método dos mínimos quadrados
popt_g, _ = curve_fit(G, yi_data, Gi_data)

# Obtendo os coeficientes ajustados da função G(y)
b0_fit, b1_fit, b2_fit, b3_fit = popt_g

# Exemplo de uso com o número complexo z = x + yi
z = complex(2, 0.3)

# Calculando M(z) para o número complexo dado usando os coeficientes ajustados
result = F(z.real, a_fit, b_fit, c_fit) + G(z.imag, b0_fit, b1_fit, b2_fit, b3_fit)

print("M(z) =", result)
print("Coeficientes ajustados da função F(x):")
print("a =", a_fit)
print("b =", b_fit)
print("c =", c_fit)
print("Coeficientes ajustados da função G(y):")
print("b0 =", b0_fit)
print("b1 =", b1_fit)
print("b2 =", b2_fit)
print("b3 =", b3_fit)
