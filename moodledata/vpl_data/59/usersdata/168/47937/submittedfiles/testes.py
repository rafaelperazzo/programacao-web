# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('digite o valor de a: '))
b=int(input('digite o valor de b: '))
b=0
a=100
for i in range(0,a,1):
    if a%(i+1)!=0:
        b=b+1
print (b)    