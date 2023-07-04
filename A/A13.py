#Faça um programa que leia um número inteiro S que representa uma quantidade de segundos. Seu programma deve imprimir quatro valores inteiros, que representem a quantidade de segundos S em dias, horas, minutos e segundos. Por exemplo, 188365 segundos representam 2 dias, 4 horas, 19 minutos e 25 segundos. Dica: lembre-se dos operadores resto e divisão inteira.
a = int(input())
segundosPdia = 86400
segundosPhora = 3600
segundosPmin = 60
dias= a//segundosPdia
restodias= a % segundosPdia
horas = restodias//segundosPhora
restohoras= restodias % segundosPhora
minutos = restohoras // segundosPmin
segundos = restohoras% segundosPmin
print(dias, horas, minutos, segundos) 
