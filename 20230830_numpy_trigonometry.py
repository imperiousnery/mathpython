import numpy as np
from scipy.optimize import curve_fit

# Função F(x) = ax^2 + bx + c (Exemplo de função polinomial para a parte real)
def F(x, a, b, c):
    return a * x**2 + b * x + c

# Função G(y) = b0 + b1y + b2y^2 + b3y^3 (Exemplo de função polinomial para a parte imaginária)
def G(y, b0, b1, b2, b3):
    return b0 + b1 * y + b2 * y**2 + b3 * y**3

# Função M(z) = F(Re(z)) + G(Im(z))
def M(z, a, b, c, b0, b1, b2, b3):
    # Obtendo a parte real (Re(z)) e a parte imaginária (Im(z)) de z
    x = z.real
    y = z.imag

    # Calculando F(Re(z)) e G(Im(z))
    f_value = F(x, a, b, c)
    g_value = G(y, b0, b1, b2, b3)

    # Calculando M(z) = F(Re(z)) + G(Im(z))
    result = f_value + g_value
    return result

# Dados hipotéticos dos zeros não triviais da função zeta de Riemann
# Aqui, usamos alguns valores arbitrários como exemplo
# Em um cenário real, você precisaria de dados reais
yi_data = np.array([0.1, 0.2, 0.3, 0.4, 0.5])  # Parte imaginária (y) dos zeros não triviais
Gi_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])  # Valores reais associados aos zeros não triviais

# Realizando o ajuste dos coeficientes usando o método dos mínimos quadrados
popt, _ = curve_fit(M, yi_data, Gi_data)

# Obtendo os coeficientes ajustados
a_fit, b_fit, c_fit, b0_fit, b1_fit, b2_fit, b3_fit = popt

# Exemplo de uso com o número complexo z = x + yi
z = complex(2, 0.3)

# Calculando M(z) para o número complexo dado usando os coeficientes ajustados
result = M(z, a_fit, b_fit, c_fit, b0_fit, b1_fit, b2_fit, b3_fit)

print("M(z) =", result)
print("Coeficientes ajustados:")
print("a =", a_fit)
print("b =", b_fit)
print("c =", c_fit)
print("b0 =", b0_fit)
print("b1 =", b1_fit)
print("b2 =", b2_fit)
print("b3 =", b3_fit)
