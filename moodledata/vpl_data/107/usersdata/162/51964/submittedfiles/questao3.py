# -*- coding: utf-8 -*-
p=int(input('Digite p:'))
q=int(input('Digite q:'))
contador1=0
contador2=0
for i in range(2,p,1):
    if p%i==0:
        contador1=contador1+1
    if contador1==0:
        i=i+1
for i in range(2,q,1):
    if q%i==0:
       contador2=contador2+1
    if contador2==0:
        i=i+1
if (q==p+2) and (contador1==0) and (contador2==0):
    print('S')
else:
    print('N')
