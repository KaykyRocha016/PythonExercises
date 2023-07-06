def primo(x):
    i=1
    j=0
    while i<=x:
        if x%i==0:
            j+=1
        i+=1
    if j==2:
        return True
    return False

n=int(input())
soma=0
i=0
for i in range (n+1):
    if primo(i)==True and i!=0:
        soma+=i
    
print(soma)
    



