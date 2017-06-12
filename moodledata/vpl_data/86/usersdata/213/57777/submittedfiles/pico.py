# -*- coding: utf-8 -*-

def pico(lista):
    if len(lista)%2==0:
        contador=0
        for i in range((len(lista)/2),-1,-1):
            if lista[i]<lista[i-1]:
                contador=contador+1
    else:
        for i in range ((len(lista)//2)+1,len(lista),1):
            if lista[i]>lista[i+1]:
                contador=contador+1
    if contador!=0:
        return (True)
    else:
        return (False)

n=int(input('Digite a quantidade de elementos da lista: '))
lista=[]
for i in range(0,n,1):
    elemento=int(input('Informe os elementos da lista: '))
    lista.append(elemento)
if pico(lista):
    print('S')
else:
    print('N')