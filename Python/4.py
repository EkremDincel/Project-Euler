from utils import number_combinations

def is_palindromic(number):
    number = str(number)
    return number[:3] == number[:2:-1]


s = 0
for a, b in number_combinations(999, 999):
    k = a*b
    if s < k and is_palindromic(k):
        s = k


print(s)
