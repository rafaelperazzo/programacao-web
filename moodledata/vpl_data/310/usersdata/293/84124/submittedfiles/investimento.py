# -*- coding: utf-8 -*-
from __future__ import division
cont=0
investimento=float(input("Digite um valor: "))
taxa=float(input("Digite uma taxa: "))
while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))

while (True):
    print("%.2f" %(investimento))
    investimento= investimento+taxa*investimento
    cont=cont+1
    if cont==10:
        break
