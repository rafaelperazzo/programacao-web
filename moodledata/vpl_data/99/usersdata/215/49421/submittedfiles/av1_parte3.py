# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n=int(input('digite n:'))
f=1
for i in range (0,n+1,1):
    if i%2==0:
        soma=soma+(1/(f*3**i))
    else:
        soma=soma+(-1/(f*3**i))
    i=i+1
    f=f+2
r=(12**(1/2))*(soma)
print('%.6f'%r)