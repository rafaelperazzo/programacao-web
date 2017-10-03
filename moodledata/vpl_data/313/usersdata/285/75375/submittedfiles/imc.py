# -*- coding: utf-8 -*-
h=float(input("digite o valor de h: "))
p=float(input("digite o valor de p: "))
IMC=(p/(h**2))
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

