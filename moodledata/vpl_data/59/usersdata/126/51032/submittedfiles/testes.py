# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n=int(input('digite o numero:'))

p=0
q=n
soma=0

while soma >1:
    p=q%10
    q=q//10
    soma=soma+p**2
print(soma)