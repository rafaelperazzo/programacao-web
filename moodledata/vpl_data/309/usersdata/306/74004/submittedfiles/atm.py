# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a=int(input("Valor a ser Sacado: R$ "))
n20= 0
n10= 0
n5= 0
n2= 0
n1= 0

while a>=20:
    n20=n20+1
    a=a-20
while a>=1:
    n10=n10+1
    a=a-10
while a>=1:
    n5=n5+1
    a=a-5
while a>=1:
    n2=n2+1
    a=a-2
while a>=1:
    n1=n1+1
    a=a-1
print("%.d"%n20)
print(0)#Como fazer para aparecer o 0 no print?
print(0)#Como fazer para aparecer o 0 no print?
print("%.d"%n2)
print("%.d"%n1)
    
    
