# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO

n=int(input('digite o valor de n:'))
soma=0
j=1
k=3
for i in range(0,n,1):
    if i%2==0:
        soma=soma+1/(j*(3**i))
        j=j+4
    else:
        soma=soma-1/(j*(3**i))
        k=k+4
print(soma)