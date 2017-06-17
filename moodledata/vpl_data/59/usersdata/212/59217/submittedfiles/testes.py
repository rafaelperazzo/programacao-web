# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite um valor:'))
x=n
i=1
while i!=0:
    ne=0
    num=n
    ne=1
    while (num//10)>0:
        ne=ne+1
        num=num//10
    soma=0
    i=ne-1
    while i>=0:
        e=n//(10**i)
        soma=soma+(e**2)
        n=n%(10**i)
        i=i-1
    print(soma)
    n=soma
    if n==1:
        print('Número Feliz')
        break
    elif n==x:
        print('Não é um número feliz')
        break