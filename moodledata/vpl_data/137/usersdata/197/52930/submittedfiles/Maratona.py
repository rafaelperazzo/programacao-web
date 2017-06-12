# -*- coding: utf-8 -*-
a=int(input('Digite a quantidade de postos:'))
b=int(input('Digite a maior distancia:'))
s=0
cont=1
for i in range (1,a+1,1):
    x=int(input('Digite a distancia dos postos de agua:'))
    d=x-s
    if d<=b:
        cont=cont+1
    s=x
if cont==a+1:
    print('S')
    
else:
    print('N')