# -*- coding: utf-8 -*-
def modulo_diferença(x,y):
    dif=x-y
    if dif<0:
        dif=dif*(-1)
        return(dif)
    else:
        return(dif)
lista=[]
degrau=0
n=int(input("Digite o número de elementos da lista: "))
for i in range(0,n,1):
    lista.append(int(input("Digite o valor do %dº elemento da lista: "%(i+1))))
for i in range(0,n-1,1):
    if modulo_diferença(lista[i],lista[i+1])> degrau:
        degrau = modulo_diferença(lista[i],lista[i+1])
print(degrau)