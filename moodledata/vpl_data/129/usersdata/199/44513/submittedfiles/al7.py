# -*- coding: utf-8 -*-
n = int(input('Digite o valor: '))
cont=0
for i in range(1,n,1):
    if n%i==0:
        print(i)
        cont=cont+i
if cont==n:
    print('Perfeito')
else:
    print('Não Perfeito')
