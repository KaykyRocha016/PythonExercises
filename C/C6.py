from re import I


n=int(input())
i=1
h=1/i

while i<n:
    i +=1
    h += 1/i
    

print(f"{h:.4f}")