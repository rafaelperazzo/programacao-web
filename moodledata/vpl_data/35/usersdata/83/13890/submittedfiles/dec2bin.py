# -*- coding: utf-8 -*-
from __future__ import division

p=int(input('Digite o valor de p:  '))
q=int(input('Digite o valor de q:  '))

r=0
s=0
a=q

while a>=1 :
    a=a//100
    r=r+1

while p>0 :
    if p%(10**r)==q :
        s=s+1
        break
    p=p//10

if s>0 :
    print ('S')
else : 
    print ('N')