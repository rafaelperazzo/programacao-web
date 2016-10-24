# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o valor de p: ')
q=input('Digite o valor de q: ')
i=1
cont1=0
cont2=0

for i in range (1,i+1,1) :
    p%i==0
    cont1=cont1+1
for i in range (1,i+1,1):
    p%i==0
    cont2=cont2+1
if cont1==1 and cont2==0 :
    if q=p+2 :
        print ('S')
    else :
        print ('N')