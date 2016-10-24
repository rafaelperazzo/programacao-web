# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o valor de p: ')
q=input('Digite o valor de q: ')
i=1
cont1=0
cont2=0

while i<=1000 :
    p%i==0
    i=i+1
    cont1=cont1+1
    break
while i<=1000:
    q%i==0
    cont2=cont2+1
    break
if cont1==1 and cont2==0 :
    if q==p+2 :
        print ('S')
    else :
        print ('N')