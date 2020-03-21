def fibonacci(i):
    x = 1
    y = 0
    z = 0
    while i > x:
        z = y
        y = x
        x = y + z
        yield x

sum_of = 0
for i in fibonacci(4000000):
    if not i%2:
        sum_of += i

print(sum_of)
