# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=[1,2,1]
n=int(input('Digite seu numero: '))
i=0
def crescente(lista):
        while i<n:
            if lista[i]<lista[i+1]:
                return True
                i=+1
        else:
            return False
print (crescente(a))