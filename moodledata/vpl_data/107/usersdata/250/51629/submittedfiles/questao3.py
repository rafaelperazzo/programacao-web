# -*- coding: utf-8 -*-
p=int(input('digite o primeiro numero:'))
q=int(input('digite o segundo numero:'))
contador1=0
contador2=0
for i in range (1,p+1,1):
    if p%i==0:
        contador1=contador1+1
for d in range (1,q+1,1):
    if q%d==0:
        contador2=contador2+1 
if contador1==2 and contador2==2:
    if q==p+2:
        print('S')
    else:
        print('N')
else:
    print('N')
