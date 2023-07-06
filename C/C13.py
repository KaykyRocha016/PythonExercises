dinheiro=int(input())
preço=int(input())
embalagens=int(input())
chocolates=dinheiro//preço
troca=chocolates

while troca>=embalagens:
    chocolates+= 1
    troca= troca-embalagens
    troca=troca+1
print(int(chocolates))

     
