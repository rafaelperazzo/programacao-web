# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite um número:'))
m=int(input('Digite um número:'))
d=1
nd=n%d
md=m%d
if nd>0 and md>0:
    d=d+1
    print(d)