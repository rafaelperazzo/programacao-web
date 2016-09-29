# -*- coding: utf-8 -*-
from __future__ import division

p=input("digite o peso")
h=input("digite a altura")

IMC=p/(h**2)

if IMC<20:
    print("ABAIXO")
if (IMC>=20) and (IMC<=25):
    print("NORMAL")
if (IMC>25) and (IMC<=30):
    print("SOBREPESO")
if (IMC>30) and (IMC<=40):
    print("OBESIDADE")
if IMC>40:
    print("OBESIDADE GRAVE")