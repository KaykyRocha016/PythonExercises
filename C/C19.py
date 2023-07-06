idade=int(input())
soma=0
maiores=0
pessoas=0
idosos=0
while idade>=0:
    soma+=idade
    if idade>=18:
      maiores+=1
    if idade>75:
        idosos+=1
    pessoas+=1
    idade=int(input())
    
média=soma/pessoas
porcentagem_idosos= (idosos/pessoas)*100
print(f"{média:.2f}")
print(maiores)
print(f"{porcentagem_idosos:.2f}%")



