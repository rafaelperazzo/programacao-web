# -*- coding: utf-8 -*-
from __future__ import division
import math
print("Cálculo dos n primeiros múltiplos de i ou de j")
n = int(input("Digite n: "))
a = int(input("Digite i: "))
b = int(input("Digite j: "))
 
multa = 0 # múltiplos de a
multb = 0 # múltiplos de b
cont = 0 # conta quantos múltiplo foram impressos
 
while cont < n:
    if multa < multb:
        print(multa)
        multa=multa + a
    elif multb < multa:
        print(multb)
        multb=multb + j
    else: # multa == multb
        print(multb)
        multb=multa + i
        multa=multb + j
    cont=cont + 1
