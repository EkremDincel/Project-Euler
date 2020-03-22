from utils.primes import primes, extend_primes_up_to_n

extend_primes_up_to_n(primes, 2_000_000)
print(sum(primes))
