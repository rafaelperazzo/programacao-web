# -*- coding: utf-8 -*-
from __future__ import division

def pico(a):
    posicao=0
    for i in range(0,len(a)-1,1):
        if a[i]>a[i+1]:
            posicao= i
            break

    cont=0
    for i in range(posicao,len(a)-1,1):
        if a[i]<=a[i+1]:
            cont=cont+1
        
    
    if cont==0 and posicao!=0:
        return True
    else:
        return False
        
n= int(input('Digite o valor de n: '))
a=[]

for i in range(0,n,1):
    a.append(input('Digite o termo: '))
    
if pico(a):
    print('S')
else:
    print('N')