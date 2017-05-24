# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO

n=int(input('digite o valor de n:'))
soma=0
j=1
for i in range(0,n,1):
    if i%2==0:
        soma=soma+1/(j*(3**i))
        j=j+2
    else:
        soma=soma-1/(j*(3**i))
        j=j+2
produto=(12**(0.5))*soma
print('%.6f'%produto)
