# -*- coding: utf-8 -*-
peso=float(input("digite o valor de p: "))
altura=float(input("digite o valor de h: "))
IMC=(peso/(altura**2))
if IMC<20:
    print("ABAIXO")
elif 20<=IMC<=25:
    print("NORMAL")
elif 25<IMC<=30:
    print("SOBREPESO")
elif 30<IMC<=40:
    print("OBESIDADE")
else:
    print("OBESIDADE GRAVE")

