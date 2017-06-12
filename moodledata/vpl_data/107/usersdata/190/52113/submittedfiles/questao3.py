# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
cont1=0
cont2=0
i1=2
i2=2
while i1<p:
    if p%i1==0:
        cont1=cont1+1
    i1=i1+1
    
    while i2<q:
        if q%i2==0:
            cont2=cont2+1
        i2=i2+1
    if cont2==0:
        if q==p+2:
            print('S')
else:
    print('N')
