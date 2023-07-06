n = int(input())
maior = 0
segundo = 0
i = 0
while i < n :
    number = int(input())
    if number >= maior or i < 1:
        segundo= maior
        maior= number
    elif number > segundo:
        segundo = number
    i += 1
print(maior)
print(segundo)

    


        