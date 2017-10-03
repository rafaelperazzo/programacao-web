# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
p = int(input(("Digite seu peso: "))
h = int(input("Digite sua altura: "))
IMC = p/h**2
if IMC<20:
    print("ABAIXO DO PESO")
if 20<=IMC<=25:
    print("PESO NORMAL")
if 25<IMC<=30:
    print("SOBREPESO")
if 30<IMC<=40:
    print("OBESIDADE")
if IMC>40:
    print("OBESIDADE MÓRBIDA")