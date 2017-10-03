# -*- coding: utf-8 -*-
peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (m): "))
IMC = peso/(altura)**2 
if IMC<20:
    print("ABAIXO")
if 20<=IMC<=25:
    print("NORMAL")
if 25<IMC<=30:
    print("SOBREPESO")
if 30<IMC<=40:
    print("OBESIDADE")
if IMC>40:
    print("OBESIDADE GRAVE")
