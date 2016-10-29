# -*- coding: utf-8 -*-
from __future__ import division

p = int(input ('insira o valor de p:'))
q = int(input ('insira o valor de q:'))



n=p
cont=0

while n>0:
    n=n//10
    cont=cont+1
    
cont2=0

while q>0:
    
    r=q%(10**cont)
    if p==r:
        cont2=cont2+1
        break
    q=q//10
    
    
if cont2>0:
    print ('S')
    
else:
    print ('N')