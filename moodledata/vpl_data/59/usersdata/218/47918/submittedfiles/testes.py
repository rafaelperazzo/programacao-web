# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite o numero de lances:'))
valor=0
for i in range(0,n,1):
    l=int(input('digite o seu lance:'))
    if lance>valor:
        valor=lance
print(valor)        
