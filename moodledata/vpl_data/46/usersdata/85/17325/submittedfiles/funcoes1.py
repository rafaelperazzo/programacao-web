# -*- coding: utf-8 -*-
from __future__ import division

def crescente(a):
    cont=0
    if a[0]<a[1]:
        cont=cont+1
    if a[len(a)-1]>a[len(a)-2]:
        cont=cont+1
    for i in range(1,len(a),1):
        if a[i]<a[i+1]:
            cont= cont+1
    if cont==len(a)-1:
        return True
    else:
        return False

n= int(input('Digite o valor de n: '))
a=[]

for i in range(0,n,1):
    a.append(input('Digite o termo: '))
    
if crescente(a):
    print('S')
else:
    print('N')