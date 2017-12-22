# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    var=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            var=var+1
        elif lista[i]>lista[i+1]:
            var=var+1
    if var==len(lista)-1:
        return (True)
    else:
        return (False)


n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...

lista=[ ]

for i in range(0,n,1):
    valor=float(input('Digite os valores da lista: '))
    lista.append(valor)
if pico(lista):
    print('S')
else:
    print('N')