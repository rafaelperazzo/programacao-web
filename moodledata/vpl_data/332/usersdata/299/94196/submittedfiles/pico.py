# -*- coding: utf-8 -*-

def pico(lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i-1]<lista[i]:
            cont+=0
            continue
        elif lista[i-1]==lista[i]:
            cont+=1
            return('N')
            break 
        elif lista[i-1]>lista[i]:
            cont+=0
            continue
        else:
            cont+=1
            return('N')
            break
    if cont==0:
        return('S')
    else:
        return('N')
    #CONTINUE..
    


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
