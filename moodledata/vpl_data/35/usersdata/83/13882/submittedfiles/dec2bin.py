# -*- coding: utf-8 -*-
from __future__ import division

p=int(input('Digite o valor de p:  '))
q=int(input('Digite o valor de q:  '))

i=0
a=q
b=0

while a>=1 :
    a=a//10
    i=i+1

while p>0 and p%(10**i)==q :
        b=b+1
        break
    p=p//10

if b>0 :
    print ('S')
else : 
    print ('N')