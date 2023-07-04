#Faça um programa que leia dois números inteiros. Após isso, seu programa deve imprimir o resultado das seguintes operações: 1) o valor da divisão real do primeiro número lido pelo segundo (imprimir com duas casas decimais); 2) o valor da divisão inteira do primeiro pelo segundo (imprimir como número inteiro); 3) o valor do resto da divisão do primeiro pelo segundo (imprimir como número inteiro).
a = int(input())
b = int(input())
divisão1 = float(a/b)
divisão2 = int(a/b)
print(f"{divisão1:.2f}")
print(divisão2)
print(a%b)
