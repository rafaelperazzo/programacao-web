# -*- coding: utf-8 -*-
from __future__ import division

def crescente (l):
    for i in range (0,len(a)-2,1):
        if (a[i+1]<a[i]):
            return False
            break
        else:
            return True
            break
    


n = input ('Digite n:')
a = []
b = []
c = []

for i in range (0,n,1):
    a.append (input ('Digite um elemento da lista a:'))
    
if crescente(a):
    print ('S')
else: 
    print ('N')
    

        

   