E = int(input())
B = int(input())
N = int(input())
V=int(input())
brancos =(B/E)*(100)
Nulos = (N/E)*100
validos = (V/E)*100
ausentes= 100 - (brancos + Nulos + validos)
print("Nulos:",f"{Nulos:.2f}%")
print("Brancos:",f"{brancos:.2f}%")
print("Validos:",f"{validos:.2f}%")
print("Ausentes:",f"{ausentes:.2f}%")


