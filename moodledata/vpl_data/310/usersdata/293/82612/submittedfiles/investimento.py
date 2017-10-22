# -*- coding: utf-8 -*-
from __future__ import division

investimento=float(input("Digite um valor: "))
valor=0
taxa=float(input("Digite uma taxa: "))

while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))

saldo=(investimento*(1+taxa))

while not((saldo==investimento((1+taxa)**10))):
    valor=valor+saldo
    print(valor)
    