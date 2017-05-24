# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
soma=0

for i in range (1,n+1,1):
    numerador=numerador+1
    denominador=numerador**2
    s=numerador/denominador
    if i%2!=0:
        soma=soma+s
    else:
        soma=soma-s
print('%.5f'%s)
        
    