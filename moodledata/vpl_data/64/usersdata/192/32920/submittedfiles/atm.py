# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
n=int(input('digite um valor:'))
if(n/20):
    d20=n/20
    print('%d'%d20)
if(n/10):
    r20=n%20
    d10=r20/10
    print('%d'%d10)
if(n/5):
    r10=r20%10
    d5=r10/5
    print('%d'%d5)
if(n/2):
    r5=r10%5
    d2=r5/2
    print('%d'%d2)
if(n/1):
    r2=r5%2
    d1=r2/1
    print('%d'%d1)
