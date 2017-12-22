# -*- coding: utf-8 -*-
n=int(input('Digite o número de postos de água: '))
m=int(input('Digite a distância intermediária máxima do atleta: '))
soma=0
cont=0
for i in range (0,n,1):
    d=int(input('Digite a distancia do posto de água: '))
    soma=d-soma
    if soma>m:
        cont=cont+1
        break
    
if cont=0:
    print('S')
else:
    print('N')
    

    