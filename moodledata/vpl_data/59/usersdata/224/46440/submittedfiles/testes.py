# -*- coding: utf-8 -*-
n=int(input('Digite n: '))
cont=0
for i in range(2,n,1):
    if n%i==0:
        
        cont==cont+i
        i=i+1
if cont==n:
    print(' perfeito ')
else:
    print(' Não é perfeito' )