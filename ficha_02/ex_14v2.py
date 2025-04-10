import math

n = int(input("Número para factorializar: "))
i = n

while i > 0:
    j = math.factorial(i)
    print(f"({n} * {i}) = {j}")
    i -= 1 