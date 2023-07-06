numero=int(input())
divisor=1
soma=0
while divisor<numero:
    teste=numero%divisor
    if teste==0:
        soma+=divisor
    divisor+=1
if soma==numero:
    print("S")
else:
    print("N")


