# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a=int(input("Valor a ser Sacado: R$ "))
n20=0
n10=0
n5=0
n2=0
n15=0

if a>=20:
    n20=n20+1
    a=a-20
elif a>=10:
    n10=n10+1
    a=a-10
elif a>=5:
    n5=n5+1
    a=a-5
elif a>=2:
    n2=n2+1
    a=a-2
elif a>=1:
    n1=n1+1
    a=a-1
print("A quantidade de notas é: \nn20 \nn10 \nn5 \nn2 \nn1
    
    
