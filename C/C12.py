n=int(input())
i=0
soma=0
maior=0
menor=0


while i<n:
    a=int(input())

    if i==0:
       maior=a
       menor=a
    
    if a>maior:
        maior=a
    
    if a<menor:
        menor=a
    
    i=i+1    
    
    soma= soma+a    



print(maior)

print(menor)
print(soma)

    

    