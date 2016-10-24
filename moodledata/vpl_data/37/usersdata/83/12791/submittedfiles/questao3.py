# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o valor de p: ')
cont1=0
n=1

for i in range (1,n+1,1) :
    p%n==0
    cont1=cont1+1
if cont1==1 :
    print ('é primo')
else :
    print ('não')