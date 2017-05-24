# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('n:'))
numerador=1
denominador=1
soma=0
for n in range(1,n+1,1):
    x=n/(n**2)
    if n%2==0:
        soma=soma-x
    else:
        soma+soma+x
print('%.5f'%soma)