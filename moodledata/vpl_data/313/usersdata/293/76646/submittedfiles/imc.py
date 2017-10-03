# -*- coding: utf-8 -*-
peso=float(input("Digite o peso: "))
altura=float(input("Digite a altura: "))
IMC=(peso/(altura**2))
if IMC<20:
    print("ABAIXO")
elif 20<=IMC<=25:
    print("NORMAL")
elif 25<=IMC<=30:
    print("SOBREPESO")
elif 30<=IMC<=40:
    print("