# -*- coding: utf-8 -*-
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
IMC = peso/(altura)**2
if IMC<20:
    print("ABAIXO")
if 20<=IMC<=25:
    print("NORMAL")

