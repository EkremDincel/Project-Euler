from math import prod
from utils.primes import extend_primes_up_to_n, primes
from utils import triangular_numbers
from utils.divisors import divisor_count


extend_primes_up_to_n(primes, 100000) # fine while i < 100000 ** 2
for i in triangular_numbers():
    if divisor_count(primes, i) > 500:
        print(i)
        break
