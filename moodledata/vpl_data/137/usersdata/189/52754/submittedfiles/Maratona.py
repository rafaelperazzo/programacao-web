# -*- coding: utf-8 -*-
n=int(input('quantidade de pontos de água:'))
d=int(input('distância entre os pontos de água:'))
for i in range(1,n+1,1):
    dp=int(input('distância entre os pontos:'))
    d=dp-dp
if d<=m:
    print('S')
else:
    print('N')
    
