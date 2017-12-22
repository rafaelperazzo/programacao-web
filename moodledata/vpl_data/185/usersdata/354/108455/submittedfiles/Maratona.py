# -*- coding: utf-8 -*-
n=int(input('digite o numero de postos de agua: '))
m=int(input('digite a distancia intermediaria maxima do atleta: '))
soma=0
cont=0
for i in range(0,n,1):
    d=int(input('digite a distancia do posto de agua: '))
    soma=d-soma
    if soma>m:
        cont=cont+1
        break
    
if cont==0:
    print('S')
else:
    print('N')