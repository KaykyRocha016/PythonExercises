A = float(input())
B = float(input())
C = float(input())
delta = B**2 - 4 *A* C
x1 = (-1*B + delta**(1/2))/(2*A)
x2 = (-1*B - delta**(1/2))/(2*A)
print(f"{x1:.2f}")
print(f"{x2:.2f}")