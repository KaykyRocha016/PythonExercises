n=input()
j=len(n)-1
for i in range(len(n)):
    if n[i]==n[j]:
        j-=1
        palindromo=True
    else:
        palindromo=False
        break

if palindromo==True:
    print("S")
else:
    print("N")



