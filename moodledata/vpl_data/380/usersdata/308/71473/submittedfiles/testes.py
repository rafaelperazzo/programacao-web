# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
i = 1
atual = 0
total = 0
anterior = -11
np = int(input('Informe o número de pessoas: '))
while i<=np:
    limanterior = atual +10
    atual = int(input('Instante: '))
    if anterior<=(atual):
        total = total + 10
        print ('entrou')
    i += 1
    
print (total)



