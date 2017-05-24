# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('n:'))
numerador=1
denominador=1
soma=0
for n in range(1,n+1,1):
    x=numerador/denominador
    numerador=numerador+1
    numerador=numerador*-1
    denominador=numerador**2
    soma=soma+x
print('%.5f'%s)