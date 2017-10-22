# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n=int(input('Digite o valor de n: '))
soma=0
i=1
while(i<=n):
    if (i%2!=0):
        soma=soma + (1)/i*3**(i-1)
    else:
        soma=soma -(1)/i*3**(i-1)
    i=i+1

print(12**0.5*(soma))