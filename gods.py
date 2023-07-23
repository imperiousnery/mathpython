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

def find_common_patterns(primes_list):
    # Encontra padrões entre os números primos
    last_digits = list(set(prime % 10 for prime in primes_list))
    first_digits = list(set(int(str(prime)[0]) for prime in primes_list))
    differences = list(set(primes_list[i + 1] - primes_list[i] for i in range(len(primes_list) - 1)))

    return last_digits, first_digits, differences

if __name__ == "__main__":
    num_primes = 100000
    primes_list = generate_primes_list(num_primes)

    last_digits, first_digits, differences = find_common_patterns(primes_list)

    # Gerar arquivo de texto
    with open("prime_patterns.txt", "w") as file:
        file.write("Últimos dígitos:\n")
        file.write(", ".join(map(str, last_digits)) + "\n\n")

        file.write("Primeiros dígitos:\n")
        file.write(", ".join(map(str, first_digits)) + "\n\n")

        file.write("Diferenças entre números primos consecutivos:\n")
        file.write(", ".join(map(str, differences)) + "\n")

    print("Dados salvos no arquivo 'prime_patterns.txt'")
