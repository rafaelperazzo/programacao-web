# -*- coding: utf-8 -*
def crescente (d,lista):
    cont=0
    for i in range (0,d-1,1):
        if lista[i]<lista[i+1]:
            cont= cont+1
    if cont==(len(lista)-1):
        return('S')
    else:
        return('N')
        
def decrescente (d,lista):
    cont=0
    for i in range (0,d-1,1):
        if lista[i]
    