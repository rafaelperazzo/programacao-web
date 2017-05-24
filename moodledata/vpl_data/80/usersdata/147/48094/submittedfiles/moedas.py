# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
i=1
v=b
cont=0
resto=0
while i//c!=0 and i<=a:
    cont=cont+1
    i=i+1
    if a%c!=0:
        resto=(i%c)//v
print(cont)
print(resto)
