# -*- coding: utf-8 -*-
from __future__ import division

def crescente (l):
    for i in range (0,len(a)-2,1):
        if (l[i+1]<l[i]):
            return False
            break
        else:
            return True
            break
    
def decrescente (l):
    for i in range (0,len(a)-2,1):
        if (l[i+1]>l[i]):
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
    
if decrescente(a):
    print ('S')
else: 
    print ('N')
    
for i in range (0,len(l)-2,1):
    if (a[i]==a[i+1]):
        print ('S')
    else:
        print ('N')

        

   