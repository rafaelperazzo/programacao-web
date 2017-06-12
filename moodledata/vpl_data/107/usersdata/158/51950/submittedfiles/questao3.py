# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
cont1=0
for i in range(2,p,1):
    if p%i==0:
        cont1=cont1+1
if cont1==0:
break 
cont2=0
for i in range(2,q,1):
    if q%i==0:
        cont2=cont2+1
if cont2==0:
break
if p+2==q:
    print('S')
else: 
    print('N')





