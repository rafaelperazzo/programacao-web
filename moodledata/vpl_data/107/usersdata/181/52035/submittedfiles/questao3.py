# -*- coding: utf-8 -*-
p=int(input('digite o valor p:'))
q=int(input('digite o valor q:'))
cont1=0
cont2=0
i=2
while i<p and i<q and q==p+2:
    if p%i==0:
        cont1=cont1+1
    elif q%i==0:
        cont2=cont2+cont1
    i=i+1
if cont1==0 and cont2==0:
    print('S')
else:
    print('N')
