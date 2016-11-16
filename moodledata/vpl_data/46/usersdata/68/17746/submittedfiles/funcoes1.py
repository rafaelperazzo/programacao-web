# -*- coding: utf-8 -*-
from __future__ import division

#programa principal

n=input('Digite n:')
a=[]
for i in range (0,n,1):
    a.append (input('Digite um elemento da lista:'))
    
#defcrescente
cont=0
for i in range (0, len(a)-1,1):
    if a[i]>a[i+1]:
        cont=cont+1
if cont==0:
    return True
else:
    return False

#defdecrescente
cont=0
for i in range (0,len(a)-1,1):
    if a[i]<a[i+1]:
        cont=cont+1
if cont==0:
    return True
else:
    return False

