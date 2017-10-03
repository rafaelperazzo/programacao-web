# -*- coding: utf-8 -*-
from __future__ import division
import math

money=int(input("Digite um valor: "))
r1=money%20
r2=r1%10
r3=r2%5
r4=r3%2
d1=money//20
d2=r1//10
d3=r2//5
d4=r3//2
d5=r4//1
if money<0:
    print("Valor inválido")
else:
    print(d1,d2,d3,d4,d5)