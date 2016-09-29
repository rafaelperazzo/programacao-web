# -*- coding: utf-8 -*-
from __future__ import division
a=float input(('Digite a: '))
b=float input(('Digite b: '))
c=float input(('Digite c: '))

Delta=float(b**2)-4*a*c
if Delta<0:
    print 'SRR'
    
if Delta>=0:
    raiz=float(Delta**(1/2))
    
    x1=float(-b+raiz)/(2*a)
    x2=float(-b-raiz)/(2*a)
    print 'x1=%.2f'%x1
    print 'x2=%.2f'%x2

