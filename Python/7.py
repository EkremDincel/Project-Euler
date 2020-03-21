primes = [2]

def extend_primes(prime_list, n):
    k = prime_list[-1]
    j = 0
    while j < n:
        k += 1
        for i in prime_list:
            if not k % i:
                break
        else:
            prime_list.append(k)
            j += 1

extend_primes(primes, 10000)
print(primes[-1])
