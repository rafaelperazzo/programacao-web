#from minha_bib import *
# -*- coding: utf-8 -*-
from __future__ import division
investimento=float(input("Digite um valor: "))
taxa=float(input("Digite uma taxa: "))
while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))

for i in range(1,11,1) :
    investimento= investimento+taxa*investimento
    print("%d) %.2f" %(i,investimento))
