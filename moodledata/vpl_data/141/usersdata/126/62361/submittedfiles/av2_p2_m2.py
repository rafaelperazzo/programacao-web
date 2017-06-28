# -*- coding: utf-8 -*-

def soma(a,b,c):
    soma=0
    d=(len(a)-1)-c
    for i in range(a[b],a[c]+1,1):
        soma=soma+a[i]
        i=i+1
    return(soma)
n=int(input('digite a quantidade de salas:'))
b=int(input('digite o número da porta de entrada:'))
c=int(input('digite o numero da porta de saida:'))

for i in range(0,n,1):
    a=[]
    m=float(input('digite a quantidade de vidas da sala:'))
    a.append(m)
print(soma(a,b,c))
