# -*- coding: utf-8 -*-
p=int(input('p:'))
q=int(input('q:'))
cont1=0
cont2=0
i=2
while i<p and i<q:
    if p%i==0 and q%i==0:
        cont1=cont1+1
        cont2=cont2+1
    i=i+1
if cont1==0 and cont2==0:
    if q==p+2:
        print('S')
else:
    print('N')