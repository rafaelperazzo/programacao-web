# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
cont=0
i=2
while i<p:
    if p%i==0:
        cont=cont+1
    i=i+1
            
while i<q:
    if q%i==0:
        cont=cont+1
    i=i+1
    
if cont==0:
    if q==p+2:
        print('S')
    else:
        print('N')
