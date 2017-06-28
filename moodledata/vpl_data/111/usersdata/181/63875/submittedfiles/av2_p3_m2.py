# -*- coding: utf-8 -*-
n=int(input('digite n:'))
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('digite o valor:'))
        
for i in range (0,len(a),1):
    for j in range (0,len(a),1):
        if a[i]!=a[j]:
           cont1=0
           cont1=cont1+1
    if cont>1:
        linha=i
for j in range (0,len(a),1):
    for i in range (0,len(a),1):
        cont2=0
        cont2=cont2+1
    if cont>1:
       coluna=j
print (a[linha,coluna])