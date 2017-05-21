# -*- coding: utf-8 -*-
n=int(input('Informe um valor:'))
cont=0
for i in range (1,n,1):
    if (n%i==0):
        print (i)
        cont=cont+1
    if (cont==n):
        print('Numero Perfeito')
    else:
        print('Numero Não Perfeito')