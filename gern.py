import numpy as np
import matplotlib.pyplot as plt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_list(limit):
    primes_list = []
    num = 2
    while len(primes_list) < limit:
        if is_prime(num):
            primes_list.append(num)
        num += 1
    return primes_list

def save_image(x, y, filename):
    plt.scatter(x, y, c='blue', marker='o')
    plt.xlabel('Índice')
    plt.ylabel('Número Primo')
    plt.title('Distribuição de Números Primos')
    plt.grid(True)

    # Adicionando anotações dos valores
    for i in range(len(x)):
        if i % 500 == 0:  # Mostrar a cada 500 números primos
            plt.annotate(str(y[i]), (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    num_primes = 10000  # Define quantos números primos queremos no gráfico
    primes_list = generate_primes_list(num_primes)

    x = np.arange(1, num_primes + 1)
    y = np.array(primes_list)

    save_image(x, y, "primes_distribution.png")
    print("Imagem salva com sucesso!")
