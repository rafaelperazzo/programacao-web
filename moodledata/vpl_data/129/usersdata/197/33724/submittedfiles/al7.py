# -*- coding: utf-8 -*-
n=int(input('Digite o valor de n:'))
d=0
for i in range(1,n,1):
    if n%i==0:
        d=d+i
        print(i)
if d==n:
    print('perfeito')
else:
    print('NÃO PERFEITO')