# -*- coding: utf-8 -*-
n=int(input('Digite n: '))
cont=0
i=2
while i<n:
    if n%i==0:
        cont==cont+i
    i=i+1
if cont==n:
    print('perfeito')
else:
    print('não é perfeito' )