# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n=int(input('digite o numero:'))

p=0
q=n
soma=0

def feliz(q):
    while q!=0:
        p=q%10
        q=q//10
        soma=soma+p**2
if soma==1:
    print('S')
    return t
else:
    print('N')