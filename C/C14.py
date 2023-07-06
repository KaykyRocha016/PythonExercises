n=int(input())
contador_de_primo=0
divisor=1
primo=1
nprimo=0
while divisor<=n:
    resto=n%divisor
    divisor+=1
    if resto==0:
      contador_de_primo+=1
if contador_de_primo==2:
   print(primo)
else:
   print(nprimo)





