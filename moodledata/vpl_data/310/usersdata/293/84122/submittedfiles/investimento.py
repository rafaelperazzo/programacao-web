# -*- coding: utf-8 -*-
from __future__ import division

investimento=float(input("Digite um valor: "))
taxa=float(input("Digite uma taxa: "))
while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))

while investimento<=investimento*((1+taxa)**10) :
    print("%.2f" %(investimento))
    investimento= investimento+taxa*investimento