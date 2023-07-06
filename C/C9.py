n= int(input())
termo=0
prox_termo=1
fibonacci=1

i=2
while i<=n+1:
    print( fibonacci,end=" ")
    fibonacci= termo + prox_termo
    termo=prox_termo
    prox_termo=fibonacci
    i+=1
    



    

