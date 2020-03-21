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

extend_primes(primes, 2_000_000)
print(sum(primes))
