# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
num=int(input('Digite um valor:'))
n=num
x=n
i=1
while i!=0:
        while num//10>=0:
            num=num//10
            ne=ne+1
            print(ne)
        i=ne-1
        soma=0
        while i>=0:
            e=n//(10**i)
            soma=soma+(e**2)
            n=n%(10**i)
        print(soma)
        n=soma
        if n==1:
            print('Número Feliz')
            break
        elif n==x:
            print('Não é um número feliz')
            break