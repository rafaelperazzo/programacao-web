# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite: '))
for i in range(2,n+1,1):
    if n%i==0:
        print('Número não primo')
        break
    