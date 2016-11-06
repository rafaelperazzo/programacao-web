# -*- coding: utf-8 -*-
from __future__ import division
n=input('digite o valor de n:')
a=[]

for i in range(0,len(a),1):
    a.append(input('digite um elemento:'))

somai=a[0]
conti=a[0]
for i in range(0,len(a),1):
    if a[i]%2==1:
        somai=somai+a[i]
        conti=conti+1

somap=a[0]
contp=a[0]
for i in range(0,len(a),1):
    if a[i]%2==0:
        somap=somap+a[i]
        contp=contp+1

print(somai)
print(somap)
print(conti)
print(contp)
print(len(a))
    
    
    
    
    
    
    
    
