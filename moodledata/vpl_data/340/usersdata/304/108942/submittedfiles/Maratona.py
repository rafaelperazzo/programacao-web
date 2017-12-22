# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de postos de água : '))
m = int(input('Digite a distância intermediária do jogador : '))
a = []
x = 0
cont = 0
for i in range (0,n,1) :
    dist = int(input('Distância do posto : '))
    if (dist-x) <= m or (dist==0) :
        cont = cont + 1
        x = dist
if (cont==n) :
    print('S')
else :
    print('N')