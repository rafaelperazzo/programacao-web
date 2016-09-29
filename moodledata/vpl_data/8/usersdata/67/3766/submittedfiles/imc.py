# -*- coding: utf-8 -*-
from __future__ import division
p=input("Digite seu peso(sem mentiras):")
h=input("Digite sua altura:")

imc=p/(h**2)
if imc<20:
    print("ABAIXO")
elif 20<=imc<=25:
    print("NORMAL")
elif 25<imc<=30:
    print("SOBREPESO")
elif 30<imc<=35:
    print("OBESIDADE")
elif imc>40:
    print("OBESIDADE GRAVE")
