# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite um número:'))
m=int(input('Digite um número:'))
d=1
if n%d==m%d:
    while n%d==m%d:
        d=d+1
        print(d)
        