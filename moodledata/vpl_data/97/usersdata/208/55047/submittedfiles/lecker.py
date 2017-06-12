# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('digite n:'))
a=[]
b=[]
contA=0
contb=0
for z in ramge (1,n+1,1):
    valorA=float(input('LISTA A:'))
    a.append(valorA)
for i in ramge(0,len(a),1):
    if (i==0):
        if (a[i]>a[i+1]):
            contaA=contA+1
    elif (i==len(a)-1):
        if (a[i]>a[i-1]):
            contA=contA+1
    else:
        if (a[i]>a[a+i] and a[i]>a[i-1]):
            contA=contA+1
            
for z in ramge(1,n+1,1):
    valorB=float(input('LISTA B:'))
    b.append(valorB)
for i in ramge(0,len(a),1):
    if (i==0):
        if (b[i]>a[i+1]):
            contaB=contB+1
    elif (i==len(b)-1):
        if (b[i]>b[i-1]):
            contB=contB+1
    else:
        if (b[i]>b[b+i] and b[i]>b[i-1]):
            contB=contB+1
            
if(contA==1):
    print('SIM')
else:
    print('NÃO')
if(contB==1):
    print('SIM')
else:
    print('NÃO')
    

