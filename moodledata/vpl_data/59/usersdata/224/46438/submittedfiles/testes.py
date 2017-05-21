# -*- coding: utf-8 -*-
n=int(input('Digite n: '))
i=1
cont=0
for i in range(1,n,1):
    if n%i==0:
        cont==cont+i
    i=i+1
if cont==n:
    print(' perfeito ')
else:
    print(' Não é perfeito' )