# -*- coding: utf-8 -*-
peso=float(input("Digite o peso (em kg): "))
alt=float(input("Digite a altura (em metros): "))
imc=peso/(alt**2)
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