# -*- coding: utf-8 -*-
from __future__ import division
import math
#[a,b,c,d]
a=input("Digite o valor de a:")
b=input("Digite o valor de b:")
c=input("Digite o valor de c:")
d=input("Digite o valor de d:")
contador=0

if a>b:
    contador==contador+1
    if b>a and b>c:
        contador==contador+1
    elif c>b and c>d:
        contador==contador+1
    elif d>c:
        contador==contador+1
    elif contador==1:
        print("'S'")
    else:
        print("'N'")
    

        