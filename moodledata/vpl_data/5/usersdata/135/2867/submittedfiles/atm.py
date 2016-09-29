# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('digite um valor:'))

if (n>=20) :
    qtde20= int(n/20)
    n= n-(qtde20*20)
elif n<20:
    qtde20=0
    
    
if n>=10 :
    qtdeDEZ = int(n/10)
    n= n-(qtdeDEZ *10)
elif n<10:
    qtdeDEZ=0
    
if n>=5 :
    qtde5= int(n/5)
    n= n-(qtde5*5)
elif n<5:
    qtde5=0
    
if n>=2 :
    qtde2= int(n/2)
    n= n-(qtde2*2)
elif n<2:
    qtde2=0
    
if n>=1 :
    qtde1= int(n/1)
    n= n-(qtde1*1)
elif n<1:
    qtde1=0
    
print qtde20
print qtdeDEZ
print qtde5
print qtde2
print qtde1