# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite o numero:'))
s=0
for a in range(1,n,1):
    if a*(a+1)*(a+2)==n:
        s=s+1
    else:
        s=s

if s!=0:
    print('triangular')
else:
    print('nao') 
    