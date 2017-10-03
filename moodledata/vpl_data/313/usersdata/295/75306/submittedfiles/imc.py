# -*- coding: utf-8 -*-
p = float(input("Digite o peso: "))
h = float(input("Digite a altura: "))
imc = p/(h**2)
if imc<20:
    print("ABAIXO")
elif 20<=imc<=25:
    print("NORMAL")
elif 25<=imc<=30:
    print("SOBREPESO")
elif 30<=imc<=40:
    print("OBESIDADE")
else imc>40:
    print("OBESIDADE GRAVE")

