# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o valor de p: ')
q=input('Digite o valor de q: ')
i=1
cont1=0
cont2=0

while i<1000 :
    p%i==0
    cont1=cont1+1
if cont1==1 :
    print ('é primo')
else :
    print ('não')