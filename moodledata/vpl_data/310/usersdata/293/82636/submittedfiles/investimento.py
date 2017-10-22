# -*- coding: utf-8 -*-
from __future__ import division

investimento=float(input("Digite um valor: "))
valor=0
taxa=float(input("Digite uma taxa: "))

while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))

saldo=investimento+(investimento*taxa)
print(saldo)

while (True):
    if saldo/investimento==(1+taxa)**10:
        continue
    valor=valor+saldo
    print(valor)
    