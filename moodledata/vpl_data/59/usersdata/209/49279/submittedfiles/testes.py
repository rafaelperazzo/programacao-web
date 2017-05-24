# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('n:'))
numerador=1
denominador=numerador**2
for n in range(1,n+1,1):
    s=numerador/denominador
    numerador=numerador+1
    numerador=numerador*-1
print('%.5f'%s)