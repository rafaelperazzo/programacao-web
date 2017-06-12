# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    if lista[0]<lista[1]:
        contador=1
        x=0
        while contador<n:
            if x==0:
                if lista[cont]<lista[cont-1]:
                    x=1
            elif x==1:
                if lista[cont]>lista[cont-1]:
                    x=2
            else:
                return (2)
            contador=contador+1
        return (1)
    else:
        return(2)


n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
a=[]
i=0
while i<n:
    valor=int(input('o numero:'))
    a.append(valor)
    i=i+1
if pico(a)==1:
    print('S')
else:
    print('N')