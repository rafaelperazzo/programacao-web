# -*- coding: utf-8 -*-
N=int(input('Digite a quantidade de postos de água durante a maratona: '))
M=int(input('Digite a distância intermediária máxima do atleta: '))
a=[ ]
for i in range (1,N+1,1):
    n=int(input('Digite a distância do posto de água número '+str(i)+' : '))
    a.append(n)
cont=0
for i in range (0,len(a)-1,1):
    if (a[i+1]-a[i])<=M:
        cont=cont+1

if cont==(len(a)-1):
    print('S')
else:
    print('N')