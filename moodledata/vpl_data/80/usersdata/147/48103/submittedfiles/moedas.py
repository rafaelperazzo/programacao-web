# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
i=1
cont=0
resto=0
while c//i!=0 and i<=a:
    i=c//i
    cont=cont+1
    i=i+1
    if c%a!=0:
        resto=(c%a)//b
print(cont)
print(resto)
