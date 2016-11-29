# -*- coding: utf-8 -*-
from __future__ import division

def listamagica(a):
    cont2=0
    for i in range(0,len(a),1):
        cont=0
        for j in range(0,len(a),1):
            if i==a[j]:
                cont=cont+1
        if cont==a[i]:
            cont2=cont2+1
    if cont2==len(a):
        retunr True
    else:
        return False
n=input('Digite n: ')
a=[]
for i in range(0,n,1):
    a.append(input('Digite valor: ')
if listamagica(a):
    print('s')
else:
    print('n')
