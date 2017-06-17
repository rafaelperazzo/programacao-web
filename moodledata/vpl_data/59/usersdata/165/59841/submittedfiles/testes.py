# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n=int(input('digite um numero:'))
x=n//100
a=x//10
b=x%10
l=b*10+a
if (l*(x%100))==n:
    print('Vampiro')
else:
    print('Nao')
