import numpy as np
import matplotlib.pyplot as plt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_array(rows, cols):
    primes_array = np.zeros((rows, cols), dtype=int)
    num = 2
    for i in range(rows):
        for j in range(cols):
            while not is_prime(num):
                num += 1
            primes_array[i, j] = num
            num += 1
    return primes_array

def save_image(array, filename):
    plt.imshow(array, cmap='viridis')
    plt.colorbar()
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    rows = 5
    cols = 5
    primes_array = generate_primes_array(rows, cols)
    print("Matriz com números primos:\n", primes_array)
    save_image(primes_array, "primes_image.png")
    print("Imagem salva com sucesso!")
