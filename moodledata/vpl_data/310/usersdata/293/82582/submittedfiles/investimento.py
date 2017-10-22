# -*- coding: utf-8 -*-
from __future__ import division

investimento=float(input("Digite um valor: "))
saldo=(investimento+(investimento*taxa))
valor=0
while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))

while (saldo/investimento)<=((1+taxa)**10):
    valor=valor+saldo
    