# -*- coding: utf-8 -*-
p=float(input("Digite o peso p: "))
h=float(input("Digite  a altura h: "))
imc=(p/(h**2))
if imc<20:
    print("ABAIXO")
elif 20<=imc and imc<=25:
    print("NORMAL")
elif 25<imc and imc<=30:
    print("SOBREPESO")
elif 30<imc and imc<=40:
    print("OBESIDADE")
else:
    print("OBESIDADE GRAVE")


