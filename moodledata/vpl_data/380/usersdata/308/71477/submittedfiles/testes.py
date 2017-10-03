# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
i = 1
atual = 0
total = 0
limanterior = -11
np = int(input('Informe o número de pessoas: '))
while i<=np:
    limanterior = atual +10
    atual = int(input('Instante: '))
    if limanterior<=(atual):
        total = total + 10
        print ('entrou')
    else:
        print ('teste')
    
    i += 1
    
print (total)



