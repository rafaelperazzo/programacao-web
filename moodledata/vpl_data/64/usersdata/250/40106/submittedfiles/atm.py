# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
n=int(input('valor a sacar:'))
a=n%20
b=a%10
c=b%5
d=c%1
if n>0:
    a1=n/20
    print('%d'%a1)
elif a!=0:
    a2=a/10
    print('%d'%a2)
elif b!=0:
    a3=b/5
    print('%d'%a3)
elif c!=0:
    a4=c/1
    print('%d'%a4)
    
    