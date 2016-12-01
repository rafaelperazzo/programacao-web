# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def peso(a):
    soma=0
    for i in range(0, a.shape[1], 1):
        soma=soma+ a[x,i]
    for i in range(0, a.shape[0], 1):
        soma=soma+ a[i,y]
    soma= soma- 2*(a[x,y])
    return soma

n= input('Digite n: ')
a=np.zeros((n,n))
x= input('Digite x: ')
y= input('Digite y: ')
for i in range(0, a.shape[0], 1):
    for j in range( 0, a.shape[1], 1):
        a[i,j]= input('Digite um valor de a: ')

print peso(a)