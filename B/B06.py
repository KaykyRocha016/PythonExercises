import math

A = float(input())
B = float(input())
C = float(input())
delta = B**2 - 4 *A* C
x1 = (-1*B + delta**(1/2))/(2*A)
x2 = (-1*B - delta**(1/2))/(2*A)
soma = x1 + x2
if delta>= 0:
    print(f"{soma:.2f}")
else:
    print(math.nan)
