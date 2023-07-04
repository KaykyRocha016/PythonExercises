#Faça um programa que leia três números reais A, B e C de uma equação do segundo grau, considerando: Ax^2 + Bx + C. Seu programa deve calcular e imprimir as as raízes da equação. Assuma que delta sempre será positivo.
a = float(input())
b = float(input())
c = float(input())
delta = b**2 - 4 *a* c
x1 = (-1*b + delta**(1/2))/(2*a)
x2 = (-1*b - delta**(1/2))/(2*a)
print(f"{x1:.2f}")
print(f"{x2:.2f}")
