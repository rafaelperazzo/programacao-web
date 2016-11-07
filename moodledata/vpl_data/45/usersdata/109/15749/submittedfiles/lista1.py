# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite o valor de n:')
a=[]
cont1=0
cont2=0
cont3=0
cont4=0

for i in range (0,n,1):
    a.append(input('Digite o elemento:'))
    
    
for j in range (0,len(a),1):    
    
    if ((a[j])%2)==0:
        cont1=cont1+1 
        cont2=cont2+a[j]
    else:
        cont3=cont3+1
        cont4=cont4+a[j]
        
print (cont4)
print (cont2)
print (cont3)
print (cont1)
print (a)
        