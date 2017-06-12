# -*- coding: utf-8 -*-
p=int(input('digite o valor p:'))
q=int(input('digite o valor q:'))
cont1=0
cont2=0
i=2
if q==p+2:
    while p%i==0 and q%i==0:
        cont=cont+1 
    i=i+1
    if cont==0:
       print('S')
    else:
       print('N')
