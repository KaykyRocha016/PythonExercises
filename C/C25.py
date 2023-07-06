numero=int(input())
div=0
div1=1
div2=2
mult=0
while mult<numero:
    div+=1
    div1+=1
    div2+=1
    mult=div*div1*div2
if mult==numero:
  print("S")
else:
   print("N")

