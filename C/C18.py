fator_1 = int(input())
fator_2= int(input())
i = 1
k = fator_1
potencia = fator_1
if fator_2 == 0:
    potencia = 1
elif fator_1 == 0 and fator_2 == 0:
    potencia = -1    
else:    
    while i < fator_2:
        j = 1
        while j < k:
            potencia += fator_1
            j += 1
        fator_1= potencia
        i += 1
print(potencia)