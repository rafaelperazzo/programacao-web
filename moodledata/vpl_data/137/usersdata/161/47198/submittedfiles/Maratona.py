# -*- coding: utf-8 -*-
N=int(input('Informe o número de postos de água:'))
M=int(input('Informe a distância intermediária máxima do atleta:'))
x=0
n1=0
for i in range(1,N+1,1):
    n=int(input('Informe a distância do posto:'))
    x=n-n1
    n=x
    if M>=x:
        print('S')
    else:
        print('N')
    