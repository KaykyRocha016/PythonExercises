#Faça um programa que leia o valor dos catetos de um triângulo retângulo e calcule a hipotenusa, de acordo com o Teorema de Pitágoras. Pesquise como extrar a raiz quadrada de um número.
cateto1 = float(input())
cateto2 = float(input())
hipotenusa =(cateto1**2 + cateto2**2)**(1/2)
print(f"{hipotenusa:.2f}")
