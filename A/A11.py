#Faça um programa que leia o salário fixo de um vendedor e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 18% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês.
salário = float(input())
vendas = float(input())
comissão = vendas * 0.18
total = salário + comissão
print(f"{total:.2f}")
