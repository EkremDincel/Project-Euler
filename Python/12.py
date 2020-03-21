from math import prod

primes = [2]

def extend_primes(prime_list, n):
    k = prime_list[-1]
    while k < n:
        k += 1
        for i in prime_list:
            if not k % i:
                break
        else:
            prime_list.append(k)


def triangular_numbers():
    i = 0
    k = 1
    while True:
        i += k
        k += 1
        yield i

def divisor_count(prime_list, n):
    l = []
    for i in prime_list:
        if not n % i:
            n //= i
            l.append(2)
        while not n % i:
            n //= i
            l[-1] += 1

        if n == 1:
            break

    return prod(l)


extend_primes(primes, 100000) # fine while i < 100000 ** 2
for i in triangular_numbers():
    if divisor_count(primes, i) > 500:
        print(i)
        break
