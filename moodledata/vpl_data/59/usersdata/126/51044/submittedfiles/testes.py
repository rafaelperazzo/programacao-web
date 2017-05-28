# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n=int(input('digite o numero:'))

p=0
q=n
soma=0
soma2=0
r=0
s=0

while q!=0:
    p=q%10
    q=q//10
    soma=soma+p**2
    if soma>1:
        r=soma
        while r!=0:
            s=r%10
            r=r//10
            soma2=soma2+s**2
print(soma2)