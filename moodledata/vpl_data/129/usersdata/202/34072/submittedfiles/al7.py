# -*- coding: utf-8 -*-
n=int(input('digite o valor de n:'))
contador=0
for i in range (1,n,1):
    if n%i==0:
    contador=contador+1
    print(i)
if contador==n:
    print('é perfeito')
else:
    print('não é perfeito')
    