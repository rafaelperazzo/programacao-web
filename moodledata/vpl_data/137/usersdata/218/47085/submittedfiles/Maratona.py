# -*- coding: utf-8 -*-
N=int(input('digite o numero de postos da prova:'))
M=int(input('digite a distancia de alcance maxima entre os postos:'))
maxima=0
minima=42195
cont=0
for i in range (0,N,1):
    p=int(input('digite a posição do posto:'))
    if p>M:
        cont=1
if cont==0:
    print('S')
else:
    print('N')
    
    