# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
cont=0
def calcularX(a,b):
    cont=0
    for i in range (a, b, 1):
        if i%2==1:
            cont=cont+1
    return cont
print(cont)    