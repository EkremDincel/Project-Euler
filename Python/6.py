sum_to = lambda n: n * (n + 1) // 2
sum_of_squares = lambda n: sum(i**2 for i in range(1, n + 1))

answer = sum_to(100)**2 - sum_of_squares(100)

print(answer)
