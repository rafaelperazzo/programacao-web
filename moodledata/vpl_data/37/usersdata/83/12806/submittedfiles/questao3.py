# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o valor de p: ')
cont1=0
n=p

while n<=p :
    n%p==0
    p=p+1
    cont1=cont1+1
if cont1==1 :
    print ('é primo')
else :
    print ('não')