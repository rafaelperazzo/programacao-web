# -*- coding: utf-8 -*-
n=int(input('número de postos: '))
x=int(input('número médio: '))
cont=0
anterior=0
for i in range(2,n+1,1):
    d=int(input('distância: '))
    if (d-anterior)<x:
        cont=cont+1
        anterior=d
if cont==0:
    print('S')
else:
    print('N')
    
    
    