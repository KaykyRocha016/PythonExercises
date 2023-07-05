a = int(input())
b = int(input())
c = int(input())
if a + b>c and a+c>b and b+c>a: 
  if a == b and b==c:
    print("EQUILATERO")
  elif  a!=b and a!=c and b!=c:
    print("ESCALENO")
  elif a ==b and a!=c or a==c and c!=b or c==b and b!=a:
    print("ISOSCELES")
else:
  print("INVALIDO")    