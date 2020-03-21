from math import sqrt

def calc_hypo(a, b):
    c = sqrt(a**2 + b**2)
    return 0 if c%1 else int(c)


a = 1000
b = 1000

while True:
    a -= 1
    if a == 0:
        b -= 1
        a = b
        if b == 0:
            break

    c = calc_hypo(a, b)
    if c and a+b+c == 1000:
        print(a * b * c)
        break

##    if c := calc_hypo(a, b) and a+b+c == 1000: # pff atama işlemi if'den çıkılınca yapılıyor
##        print(a * b * c)
##        break
