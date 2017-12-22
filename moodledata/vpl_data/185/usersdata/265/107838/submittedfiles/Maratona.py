# -*- coding: utf-8 -*-
N=int(input('digite a quantidade de postos de água: '))
M=int(input('digite a distâcia intermediaria do atleta: '))
cont=0
soma=0
for i in range(0,N,1):
    x9=int(input('digite a distancia: '))
    y=x9-soma
    if y>M:
        print('N')
        cont=cont+1
        break
    soma=soma+y
if cont==0:
    print('S')
