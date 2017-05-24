# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
a=int(input('Digite um número:'))
b=int(input('Digite um número:'))
c=int(input('Digite um número:'))
qt_a=c//a
qt_b=0
while qt_a>=0:
    troco=c%a
    if troco%a==0:
        qt_a=troco//a
    if troco%b==0:
        qt_b=troco//b
        break
    if troco%b==1:
        qt_a=qt_a-1
print(qt_a)
print(qt_b)
