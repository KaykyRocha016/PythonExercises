a = float(input())
if a>0 and a // 4 == a/4 and a/100 != a//100:
    print(1)
elif a>0 and a//400 == a/400:
    print(1)
elif a <=0 or a/2 != a//2:
    print(-1)
else:
    print(0)