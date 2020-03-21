def sequence(n):
    return 3*n + 1 if n % 2 else n//2

def chain_lenght(n):
    k = 0
    while True:
        k += 1
        n = sequence(n)
        if n == 1:
            break
    return k

s = 0
answer = 0
for i in range(1, 1_000_000):
    k = chain_lenght(i)
    if k > s:
        s = k
        answer = i

print(answer)
