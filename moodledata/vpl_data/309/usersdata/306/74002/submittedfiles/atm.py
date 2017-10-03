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

if a>=20:
    n20= a//20
    resto20=a%20
elif resto20>=10:
    n10=a//10
    resto10=resto20%10:
elif resto10=>5:
    n5=a//5
    resto5=resto10%5
elif resto5=>2:
    n2=a//2
    resto2=resto10%2   
elif resto2=>1:
    n1=a//1
    resto1=resto10%1 
    
    
