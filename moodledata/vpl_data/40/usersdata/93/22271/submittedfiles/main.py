# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
m=input('m: ')
e=input('epsilon: ')
def abs(x):
    return (x**2)**0.5
def pi(m):
    pi=3
    i=1
    while True:
        termo= ((-1)**(i+1)*4/(2*i*(2*i+1)*(2*i+2))
        if i<m:
            break
        pi=pi+termo
        i=i+1
print pi(m)