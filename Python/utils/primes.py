primes = [2]

def extend_primes_by_n(prime_list, n):
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


def extend_primes_up_to_n(prime_list, n):
    k = prime_list[-1]
    while k < n:
        k += 1
        for i in prime_list:
            if not k % i:
                break
        else:
            prime_list.append(k)
