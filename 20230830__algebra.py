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
    last_digits = [prime % 10 for prime in primes_list]
    first_digits = [int(str(prime)[0]) for prime in primes_list]
    differences = [primes_list[i + 1] - primes_list[i] for i in range(len(primes_list) - 1)]

    return last_digits, first_digits, differences

if __name__ == "__main__":
    num_primes = 100000
    primes_list = generate_primes_list(num_primes)

    last_digits, first_digits, differences = find_common_patterns(primes_list)

    print("Últimos dígitos mais comuns:", max(set(last_digits), key=last_digits.count))
    print("Primeiros dígitos mais comuns:", max(set(first_digits), key=first_digits.count))

    most_common_difference = max(set(differences), key=differences.count)
    print("Diferença mais comum entre números primos consecutivos:", most_common_difference)
