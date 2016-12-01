# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
m=float(input('m: '))
e=input('epsilon: ')
def abs(x):
    return (x**2)**0.5
def pi(m):
    p=3
    i=1
    while i<=m:
        termo= ((-1)**(i+1)*4/(2*i*(2*i+1)*(2*i+2))
        p=p+termo
        i=i+1
    return p
print pi(m)