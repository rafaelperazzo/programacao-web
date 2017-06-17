# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite um valor'))
x=n
cont=0
while cont=0:
    num=n
    ne=0
    while num//10>0:
        num=num//10
        ne=ne+1
    i=ne-1
    soma=0
    while i<=0:
        e=n//(10**i)
        soma=soma+(e**2)
        n=n%(10**i)
    n=soma
    if n==1:
        print('Número Feliz')
        break
    elif n==x:
        print('Não é um número feliz')