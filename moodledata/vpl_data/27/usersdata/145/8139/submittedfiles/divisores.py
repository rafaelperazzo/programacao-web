# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input("Digite n: "))
a = int(input("Digite a: "))
b = int(input("Digite b: "))
 
multa = 0 # múltiplos de a
multb = 0 # múltiplos de b
cont = 0

while cont < n:
    if multa < multb:
        print(multa)
        multa=multa + a
    elif multb < multa:
        print(multb)
        multb=multb + b
    else: # multa == multb
        print(multb)
        multb=multa + a
        multa=multb + b
    cont=cont + 1
