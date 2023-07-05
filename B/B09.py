a = int(input())
b = int(input())
c = int(input())
        
if a > b and a > c:
    maior = a
    a = c
    c = maior
elif b > c:
    maior = b
    b = c
    c = maior
if a > b:
    meio = a
    a = b
    b = meio    

print(a)
print(b)
print(c)