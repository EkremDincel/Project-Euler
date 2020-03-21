from math import prod
from itertools import combinations

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

extend_primes(primes, 10000)

def d(n):
    l = []
    for i in primes:
        while not n % i:
            n //= i
            l.append(i)

        if n == 1:
            break
    return sum(set(prod(j) for i in range(len(l)) for j in combinations(l, i)))

# another function
def d(n):
    dic = {}
    k = n
    for i in primes:
        if not n % i:
            n //= i
            dic[i] = 1
        while not n % i:
            n //= i
            dic[i] += 1

        if n == 1:
            break
    return prod((i**(j+1) -1) / (i-1) for i, j in dic.items()) - k   


def is_amicable(n):
    t = d(n)
    if t == n: return False
    return n == d(t)


s = 0
for i in range(2, 10000):
    if is_amicable(i):
        s += i

print(s)
