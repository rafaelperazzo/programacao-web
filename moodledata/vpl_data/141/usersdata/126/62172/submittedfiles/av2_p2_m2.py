# -*- coding: utf-8 -*-

def soma(a,b,c):
    soma=0
    for i in range(b,c,1):
        soma=soma+a[i]
    return(soma)
n=int(input('digite a quantidade de salas:'))
b=int(input('digite o número da porta de entrada:'))
c=int(input('digite o numero da porta de saida:'))

for i in range(0,n,1):
    a=[]
    n=int(input('digite a quantidade de vidas da sala:'))
    a.append(n)
print(soma(a,b,c)
