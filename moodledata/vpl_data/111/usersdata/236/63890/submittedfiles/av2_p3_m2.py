# -*- coding: utf-8 -*-
import numpy as np
n= int(input('Dimensão da matriz'))
a= np.zeros((n,n))
ll=[]
lc=[]

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[0],1):
        a[i,j]= input('Digite o valor:')

somalinha=0    
somacoluna=0
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[0],1):
        somalinha=somalinha + a[i,j]
        somacoluna=somacoluna+ a[j,i]
    ll.append(somalinha)
    lc.append(somacoluna)
    print(ll)
    print(lc)

linha=0
for i in range(0,len(ll),1):
    cont1=0
    for j in range(0,len(ll),1):
        if ll[i]!=ll[j]:
            cont1=cont1+1
    if cont1>1:
        linha=i
        break
coluna=0
for i in range(0,len(lc),1):
    cont2=0
    for j in range(0,len(lc),1):
        if lc[i]!=lc[j]:
            cont2=cont2+1
    if cont2>1:
        coluna=i
        break

print(a[linha,coluna])


    


    
    
    

    
    
        

    


