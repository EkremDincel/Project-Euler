def fibonacci(i):
    x = 1
    y = 0
    z = 0
    while i > x:
        z = y
        y = x
        x = y + z
        yield x


def find_largest_prime_factor(n):
    i = 2
    while i * i <= n:
        while not n % i:
            n //= i
            if i * i > n:
                break
        i += 1
        
    return n


def number_combinations(a, b):
    while True:
        yield a, b
        a -= 1
        if a == 0:
            a = b
            b -= 1
            if b == 0:
                return
            

def triangular_numbers():
    i = 0
    k = 1
    while True:
        i += k
        k += 1
        yield i
