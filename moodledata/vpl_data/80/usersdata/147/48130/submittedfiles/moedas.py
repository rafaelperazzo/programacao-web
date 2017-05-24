# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
cont=0
resto=0
while c/a!=0:
    cont=cont+1
    a=c//a
    if c%a!=0:
        resto=(c%a)//b
print(cont)
print(resto)