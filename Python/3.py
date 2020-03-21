def find_largest_prime_factor(n):
    i = 2
    while i * i <= n:
        while not n % i:
            n //= i
            if i * i > n:
                break
        i += 1
        
    return n


print(find_largest_prime_factor(600851475143))

##def find_largest_prime_factor(n):
##    i = 2
##    while i < n:
##        if not n % i:
##            n //= i
##        else:
##            i += 1
##        
##    return i


## test
exit()
from sympy import factorint
def gpf(n):
    return max(factorint(n).keys())

for i in range(2, 10000):
    assert gpf(i) == find_largest_prime_factor(i)
