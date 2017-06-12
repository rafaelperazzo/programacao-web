# -*- coding: utf-8 -*-
def pico(lista):
    if lista[0]<lista[1]:
        contador=1
        i=0
        while contador<n:
            if i==0:
                if lista[contador]<lista[contador-1]:
                    i=1
            elif i==1:
                if lista[contador]>lista[contador-1]:
                    i=2
            else:
                return (2)
            contador=contador+1
        return (1)
    else:
        return (2)
n=int(input('Digite o numero de elementos que a lista possui:'))
a=[]
i=0
while i<n:
    numero=int(input('Digite um numero da lista:'))
    a.append(numero)
    i=i+1
if pico(a)==1:
    print('S')
else:
    print('N')