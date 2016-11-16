# -*- coding: utf-8 -*-
from __future__ import division
#função
def elementoscomuns (a,b):
    cont=0
    for x in range(0,len(b),1):
        for i in range(0,len(a),1):
            if a[i]==b[x]:
                cont=cont+1
    return cont
        
#entradas e programa principal
n=input('Digite um valor n:')
m=input('Digite um valor m:')

a=[]
b=[]

for i in range(0,n,1):
    a.append(input('Digite um valor:'))
for i in range(0,m,1):
    b.append(input('Digite um valor:'))
#saídas

print elementoscomuns(a,b)