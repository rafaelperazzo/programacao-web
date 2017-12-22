# -*- coding: utf-8 -*-
def modulo_diferenca(x,y):
    dif=x-y
    if dif<0:
        dif=dif*(-1)
        return(dif)
    else:
        return(dif)
lista=[]
degrau=0
n = int(input('Digite o numero de elementos da lista: '))

while(true):
    if n<2:
        n = int(input('Digite o numero de elementos da lista: '))
    else:
        break
    
for i in range(0,n,1):
    lista.append(int(input('Digite o valor do %d elemento da lista: ' %(i+1))))
for i in range(0,n-1,1):
    if modulo_diferenca(lista[i],lista[i+1])>degrau:
        degrau = modulo_diferenca(lista[i],lista[i+1])
print(degrau)

