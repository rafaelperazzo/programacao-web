# -*- coding: utf-8 -*-
p = float(input("Digite o peso: "))
h = float(input("Digite a altura: "))
i = p/(h**2)
if i<20:
    print("ABAIXO")
elif 20<=i<=25:
    print("NORMAL")
elif 25<=i<=30:
    print("SOBREPESO")
elif 30<=i<=40:
    print("OBESIDADE")
elif i> 40:
    print("OBESIDADE GRAVE")

