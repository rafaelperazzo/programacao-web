# -*- coding: utf-8 -*-
n=int(input('Digite valor de n: '))
soma=0
for i in range (1,n,1):
    if n%i==0:
        soma=soma+i
if soma==n:
    print('sim')
else:
    print('não')