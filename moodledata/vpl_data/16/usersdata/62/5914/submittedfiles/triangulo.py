# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA
    
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
c=int(input("Digite o valor de c: "))

#PROCESSAMENTO

if a<(b+c):
    print("S")
    if a**2==(b**2)+(c**2):
        print("Re")
    elif a**2>(b**2)+(c**2):
        print("Ob")
    else:
        print("Ac")
    if a==b==c:
        print("Eq")
    elif b==c!=a:
        print("Is")
    else:
        print("Es")
else:
    print("N")
        
