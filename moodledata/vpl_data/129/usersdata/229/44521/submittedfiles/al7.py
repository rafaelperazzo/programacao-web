# -*- coding: utf-8 -*-

A=int(input('digite o valor de A:'))
cont=0
for i in range(1,A,1):
    if A%i==0:
        print(i)
        cont=cont+i
if cont==A:
    print('perfeito')
else:
    print('não perfeito')