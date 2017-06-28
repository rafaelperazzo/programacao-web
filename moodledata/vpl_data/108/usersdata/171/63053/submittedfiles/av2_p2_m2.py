# -*- coding: utf-8 -*-
def vidas(a,x,y):
    soma=0
    for i in range(x,y+1,1):
        soma=soma+ a[i]
    return(soma)
n=int(input('digite o numero de salas:'))
a=[]
for i in range(0,n,1):
    valor=int(input('digite a quantidade de vidas de cada porta:'))
    a.append(valor)
x=int(input('digite o numero da porta de entrada:'))
y=int(input('digite o numero da porta de saida:'))
c=vidas(a,x,y)
print(c)


