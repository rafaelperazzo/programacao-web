# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))

y=n
digitos=1
while y>0:
    if y//10!=0:
        digitos=digitos+1
    y=y//10

a=n
exp=digitos
soma=0
for i in range (0,digitos,1):
    r=a%(10**exp)
    soma=r*(2**i)
    exp=exp-1
    a=a//10
 

    