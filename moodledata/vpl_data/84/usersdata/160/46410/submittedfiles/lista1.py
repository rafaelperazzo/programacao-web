# -*- coding: utf-8 -*-
from __future__ import division


n=int(input('Digite n:'))

i=1
cont=0
while i<n:
    nu=int(input('Digite a próxima:'))
    if i%2==1:
        cont=cont+i
        
    i=i+1
    
print(cont)

    
