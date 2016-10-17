# -*- coding: utf-8 -*-
from __future__ import division
#COMECE AQUI ABAIXO
x=1
c=1
s=0
b=input('Digite o valor binario:')
while x<b:
    b=b//10
    c=c+1
    s =s+c
print s