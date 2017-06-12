# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
contador=0
i=2
while i<p and p%2!=0:
    if p%i==0: 
        contador=contador+1
    i=i+1
    while i<q and q%2!=0:
        if q%i==0:
            contador=contador+1
        i=i+1
if contador==0:
    print('S')
else:
    print('N')

    


