# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=[1,2,1]
n=int(input('Digite seu numero: '))
cont= 0
def crescente(lista):
        while (cont<n):
            if lista[cont]<lista[cont+1]:
                return True
                cont=+1
            else:
                return False
print (crescente(a))