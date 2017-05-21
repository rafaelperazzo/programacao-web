# -*- coding: utf-8 -*-
N=int(input('Informe o número de postos de água:'))
M=int(input('Informe a distância intermediária máxima do atleta:'))
x=0
for i in range(1,N+1,1):
    n=int(input('Informe a distância do posto:'))
while M<=n:
    x=42195-M
print('S')
if M>n:
    print('N')
    