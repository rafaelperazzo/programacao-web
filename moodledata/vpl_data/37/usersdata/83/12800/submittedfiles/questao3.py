# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o valor de p: ')
cont1=0
n=1

while n<=1000 :
    p%n==0
    cont1=cont1+1
    n=n+1
    break
    if cont1==1 :
        print ('é primo')
    else :
        print ('não')