# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n=int(input('digite n:'))
soma=0
i=0

while n>0:
    resto=n%2
    n=n//2
    soma=soma+resto*10**i
    i=i+1