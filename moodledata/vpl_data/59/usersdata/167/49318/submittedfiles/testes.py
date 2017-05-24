# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
soma=0
numerador=1 
for numerador in range (1,n+1,1):
    numerador=numerador+1
    s=numerador/(numerador**2)
    if numerador%2!=0:
        soma=soma+s
    else:
        soma=soma-s
print('%.5f'%s)
        
    