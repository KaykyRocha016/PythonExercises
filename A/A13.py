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
