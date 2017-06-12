# -*- coding: utf-8 -*-
n =int(input('Digite a quantidade de elementos da lista: '))
lista=[]

for i in range(0,n,1):
    numero=int(input('Informe um número:'))
    lista.append(numero)
    
def pico(lista):
    if lista[0]<lista[1]:
        i=0
        cont=1
        while cont<n:
            if i==0:
                if lista[cont]>lista[cont]-1:
                    i=2
            elif i==1:
                return True
            cont=cont+1
        return (1)    
    else:
        return False
        


if pico(lista)==1:
    print('S')
else:
    print('N')
    