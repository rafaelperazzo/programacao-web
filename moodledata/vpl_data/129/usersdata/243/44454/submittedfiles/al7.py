# -*- coding: utf-8 -*-
n=int(input('digite o n:'))
con=0

for i in range(1,n,1):
    if n%i==0:
    cont=cont+i

if cont==n:
    print('perfeito')
else:
    print('não perfeito')