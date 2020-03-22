from utils import fibonacci

s =sum(i for i in fibonacci(4000000) if not i%2) 

print(s)
