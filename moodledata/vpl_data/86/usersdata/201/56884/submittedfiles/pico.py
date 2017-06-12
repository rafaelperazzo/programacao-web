# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    if lista[0]<lista[1]:
        cont=1
        i=1
        while cont<n:
            if i==0:
                if lista[cont]<lista[cont-1]:
                    i=1
            elif i==1:
                if lista[cont]>lista[cont-1]:
                    i=2
            else:
                return (2)
            cont=cont+1
        return (1)
    else:
        return (2)


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a=[]
i=0
while r<n:
    valor=int(inptut('Digite um valor:'))
    a.append(valor)
    i=i+1
if pico(lista)==1:
    print('S')
else:
    print('N')