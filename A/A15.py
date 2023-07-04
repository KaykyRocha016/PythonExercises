#Faça um programa que leia um número inteiro E de eleitores de um município, um número inteiro B que representa o número de votos brancos, um número N de votos nulos e um número V de votos válidos. O programa deve calcular e escrever o percentual que cada um representa em relação ao total de eleitores, além da porcentagem de ausentes. 
e = int(input())
b = int(input())
n = int(input())
v=int(input())
brancos =(b/e)*(100)
nulos = (n/e)*100
validos = (v/e)*100
ausentes= 100 - (brancos + nulos + validos)
print("Nulos:",f"{nulos:.2f}%")
print("Brancos:",f"{brancos:.2f}%")
print("Validos:",f"{validos:.2f}%")
print("Ausentes:",f"{ausentes:.2f}%")


