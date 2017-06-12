# -*- coding: utf-8 -*-

def pico(lista):
    cont=0
    for i in range (0,len(lista)//2,1):
        if lista[i]>lista[i+1]:
            return (False)
    for i in range ((len(lista)//2)+1,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)//2:
        return(True)
    else:
        return(False)


n = int(input('Digite a quantidade de elementos da lista: '))
L=[]
for i in range(0,n,1):
    valor=int(input('digite o valor:'))
    L.append(valor)
if pico(L):
    print('S')
else:
    print('N')
