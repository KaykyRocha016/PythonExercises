a=1
soma_par=0
soma_impar=0
soma=0
while a!=0:
    a=int(input())
    if a%2==0:
        soma_par+=a
    else:
        soma_impar+=a
    soma+=a
print(soma_par)
print(soma_impar)
print(soma)