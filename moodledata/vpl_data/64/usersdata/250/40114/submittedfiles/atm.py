# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
n=int(input('valor a sacar:'))
a=n%20
b=a%10
c=b%5
e=c%2
d=e%1
if n>0:
    a1=n/20
    print('%d'%a1)
if a>=0:
    a2=a/10
    print('%d'%a2)
if b>=0:
    a3=b/5
    print('%d'%a3)
if c>=0:
    a4=c/2
    print('%d'%a4)
if e>=0:
    a5=e/1
    print('%d'%a5)
    
    