from math import prod
from utils.primes import primes

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

def sum_of_divisors(n):
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













###---------------------------
def ebob(x,y):
	while y:
		r=x
		x=y
		y=r%y
	return x

def ekok(x,y):
	return x*y/ebob(x,y)

def eboblar(args):
    f, s, loop = args[0], args[1], args[2:]
    l = ebob(f, s)
    for i in loop:
        l = ebob(l, i)
    return l

def ekoklar(args):
    f, s, loop = args[0], args[1], args[2:]
    l = ekok(f, s)
    for i in loop:
        l = ekok(l, i)
    return l

