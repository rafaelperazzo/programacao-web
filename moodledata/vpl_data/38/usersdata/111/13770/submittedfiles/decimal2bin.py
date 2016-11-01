# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite um Número: ')

i=1
a=n//10
while a>0:
    i=i+1
    a=a//10
x=i-1
t=0
b=n
soma=0
while t<=x:
    c=(b%10)
    b=(b//10)
    
    soma=soma + (c*(2**t))
    t=t+1
print soma