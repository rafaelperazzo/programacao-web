# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=[1,2,1]
n=int(input('Digite seu numero: '))

def crescente(lista):
    for i in range (0,n,1):
        while lista[i]<lista[i+1]:
            return True
        else:
            return False
print (crescente(a))