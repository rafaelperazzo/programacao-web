# -*- coding: utf-8 -*-
n =int(input('Digite a quantidade de elementos da lista: '))
lista=[]
i=0 
for i in range(0,n,1):
    numero=int(input('Informe um número:'))
    lista.append(numero)
    i=i+1
    
def pico(lista):
    if lista[0]<lista[1]:
        i=0
        cont=1
        while cont<n:
            if i==0:
                if lista[cont]<lista[cont]-1:
                    i=1
            elif i==1:
                if lista[cont]>lista[cont]-1:
                    i=2
            else:        
                return (2)
            cont=cont+1
        return (1)    
    else:
        return (2)
        


if pico(lista)==1:
    print('S')
else:
    print('N')
    