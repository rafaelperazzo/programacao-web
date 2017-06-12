# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    if lista[0]<lista[1]:
        cont=1
        r=1
        while cont<n:
            if r==0:
                if lista[cont]<lista[cont-1]:
                    r=1
            elif r==1:
                if lista[cont]>lista[cont-1]:
                    r=2
            else:
                return (2)
            cont=cont+1
        return (1)
    else:
        return (2)


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a=[]
r=0
while r<n:
    valor=int(inptut('Digite um valor:'))
    a.append(valor)
    r=r+1
if pico(a)==1:
    print('S')
else:
    print('N')