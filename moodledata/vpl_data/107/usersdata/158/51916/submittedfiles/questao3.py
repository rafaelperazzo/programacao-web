# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
cont=0
for i in range(2,p,1):
    if p%i==0:
        cont=cont+1
if cont==0:
    break
cont=0
for i in range(2,q,1):
    if q%i==0:
        cont=cont+1
if cont==0:
    break
p=q+2





