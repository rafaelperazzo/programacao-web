# -*- coding: utf-8 -*-
from __future__ import division

n= int(input ('insira um valor para n:'))

a=[]

for i in range (0,n+1,1):
    a.append(input ('insira o valor:')) 
    
cont=0
cont2=0
s1=0
s2=0

for j in range (0,len(a),1):
    if a[j]%2==0:
        s1=s1+1
        cont=cont+a[j]
    else: 
        s2=s2+1
        cont2=cont2+1
        
print (cont2)
print (cont)
print (s2)
print (s1)
print (a)
