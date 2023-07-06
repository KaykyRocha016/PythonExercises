idade=int(input())
i=0
maior=0
contador_maiores=0
while i<idade:
    altura_vela=int(input())
    if altura_vela>maior:
        contador_maiores=1
        maior=altura_vela
    elif altura_vela==maior:
        contador_maiores+=1
    i+=1    
print(contador_maiores)

