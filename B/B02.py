limite = int(input())
multa = float(input())
adicional= float(input())
velocidade = int(input())
total = multa + adicional*(velocidade-limite)
if velocidade>limite:
 print(f"{total:.2f}")
else:
    print(f"{0:.2f}") 