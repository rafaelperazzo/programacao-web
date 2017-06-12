# -*- coding: utf-8 -*-
p=int(input('digite o valor p:'))
q=int(input('digite o valor q:'))
cont=0
i=2
while i<p and i<q and q==p+2:
    if p%i==0 and q%i==0:
        cont=cont+1 
    i=i+1
if cont==0:
    print('S')
else:
    print('N')
