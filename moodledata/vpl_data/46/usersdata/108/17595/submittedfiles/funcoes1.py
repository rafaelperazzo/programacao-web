# -*- coding: utf-8 -*-
from __future__ import division

n = input ('Digite n:')
a = []
b = []
c = []

for i in range (0,n,1):
    a.append (input ('Digite um elemento da lista a:'))
    
#Para a:
for i in range (0,len(a)-2,1):
    if (a[i+1]<a[i]):
        print ('N')
        break
    else:
        print ('S')
        

   