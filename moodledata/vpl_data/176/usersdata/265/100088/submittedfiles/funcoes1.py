# -*- coding: utf-8 -*-
def crescente(n,lista):
    cont=0
    for i in range (0,n-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==(len(lista)-1):
        return('S')
    else:
        return('N')

print(crescente(6,[1,2,3,4,5,6]))