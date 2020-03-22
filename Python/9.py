from math import sqrt
from utils import number_combinations

def calc_hypo(a, b):
    c = sqrt(a**2 + b**2)
    return 0 if c%1 else int(c)


for a, b in number_combinations(1000, 1000):
    c = calc_hypo(a, b)
    if c and a+b+c == 1000:
        print(a * b * c)
        break

##    if c := calc_hypo(a, b) and a+b+c == 1000: # pff atama işlemi if'den çıkılınca yapılıyor
##        print(a * b * c)
##        break
