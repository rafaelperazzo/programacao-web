# -*- coding: utf-8 -*-
h=float(input("digite o valor de h: "))
p=float(input("digite o valor de p: "))
imc=(p/(h**2))
if imc<20:
    print("ABAIXO")
elif 20<=imc<=25:
    print("NORMAL")
elif 25<imc<=30:
    print("SOBREPESO")
elif 30<imc<=40:
    print("OBESIDADE")
else:
    print("OBESIDADE GRAVE")

