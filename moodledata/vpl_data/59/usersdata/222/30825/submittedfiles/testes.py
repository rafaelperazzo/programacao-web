# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite n: '))
for i in range (2,n,1):
    if n%i==0:
        contador=contador+1
if contador==0:
    print('primo')
else:
    print('não primo')