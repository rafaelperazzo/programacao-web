# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('n:'))
soma=0
for i in range(1,n+1,1):
    x=i/(i*i)
    if n%2==0:
        soma=soma-x
    else:
        soma=soma+x
print('%.5f'%soma)