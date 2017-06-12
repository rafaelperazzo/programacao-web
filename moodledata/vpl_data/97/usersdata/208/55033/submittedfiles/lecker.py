# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('digite n:'))
a=[]
b=[]
cont A=0
cont b=0
for z in ramge(1,n+1,1):
    valor A= float(input('LISTA A:'))
    a.append(valor A)
for i in ramge(0,len(a),1):
    if (i==0):
        if (a[i]>a[i+1]):
            conta A=cont A+1
    elif (i==len(a)-1):
        if (a[i]>a[i-1]):
            cont A=cont A+1
    else:
        if (a[i]>a[a+i] and a[i]>a[i-1]):
            cont A=cont A+1
            
for z in ramge(1,n+1,1):
    valor B= float(input('LISTA B:'))
    b.append(valor B)
for i in ramge(0,len(a),1):
    if (i==0):
        if (b[i]>a[i+1]):
            conta B=cont B+1
    elif (i==len(b)-1):
        if (b[i]>b[i-1]):
            cont B=cont B+1
    else:
        if (b[i]>b[b+i] and b[i]>b[i-1]):
            cont B=cont B+1
            
if(cont A==1):
    print('SIM')
else:
    print('NÃO')
if(cont B==1):
    print('SIM')
else:
    print('NÃO')
    

