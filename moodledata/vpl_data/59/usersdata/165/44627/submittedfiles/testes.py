# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite o numero:'))
for a in range(1,n,1):
    if a*(a+1)*(a+2)==n:
        print('triangular')
    else:
        print('nao')