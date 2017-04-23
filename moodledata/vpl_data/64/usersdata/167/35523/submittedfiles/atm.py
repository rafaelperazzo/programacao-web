# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
n=int(input('digite n:'))
n20=(n-n%20)/20
if n20>0:
    n=n%20
n10=(n-n%10)/10
if n10>0:
    n=n%10
n5=(n-n%5)/5
if n5>0:
    n=n%5
n2=(n-n%2)/2
if n2>0:
    n=n%2
n1=(n-n%1)/1
if n1>0:
    n=0
    
    print('n20 é %.f'%n20)
    print('n10 é %.f'%n10)
    print('n5 é %.f'%n5)
    print('n2 é %.f'%n2)
    print('n1 é %.f'%n1)
    