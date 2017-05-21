# -*- coding: utf-8 -*-
n=int(input('Digite valor n: '))
cont=0
for i in range (2,n,1):
    if n%1==0:
        cont=cont+1
if cont==0:
    print('Primo')
else:
    print('Nao primo')
    