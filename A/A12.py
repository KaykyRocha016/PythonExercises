
import math

altura = float(input())
largura = float(input())
valor = float(input())
rendimento = float(input())
area = altura * largura
latas = area/rendimento
latasint = math.ceil(latas)
custo = latasint * valor
print(latasint) 
print(f"{custo:.2f}")