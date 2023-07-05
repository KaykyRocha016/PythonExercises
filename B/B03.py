idade = int(input())
if idade < 16 or idade >= 70:
    print("DISPENSADO")
elif idade>=16 and idade<18:
        print("FACULTATIVO")
else:
    print("OBRIGATORIO")