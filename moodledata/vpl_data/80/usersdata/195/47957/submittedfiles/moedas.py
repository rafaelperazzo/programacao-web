# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite a :'))
b=int(input('digite b :'))
c=int(input('digite c :'))
i=1
cont=0
while a>b:
    qa=b-1
    i=i+1
    cont=cont+1
print(qa)
while a<b:
    qb=b-1
    i=i+1
    cont=cont+1
print(qb)
if cont!=0:
    print('S')
else:
    print('N')
