# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o valor de p: ')
q=input('Digite o valor de q: ')
a=p
b=q
i=1
cont1=0
cont2=0

for i in range (1, p+1, 1) :
    p%a==0
    cont1=cont1+1
    a=a+1
if cont1==1 :
    print ('é primo')
else :
    print ('N')