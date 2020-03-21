from itertools import product

def is_palindromic(number):
    number = str(number)
    return number[:3] == number[:2:-1]


a = 999
b = 999

s = 0
while True:
    a -= 1
    if a == 0:
        a = 999
        b -= 1
        if b == 0:
            break

    k = a*b
    if s < k and is_palindromic(k):
        s = k


print(s)
