# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o valor de p: ')
q=input('Digite o valor de q: ')

if p%[2,p-1]==0 :
    if q%[2,q-1]==0 :
        if q==p+2:
            print ('S')
        else :
            print ('N')
    else :
        print ('N')
else : 
    print ('N')