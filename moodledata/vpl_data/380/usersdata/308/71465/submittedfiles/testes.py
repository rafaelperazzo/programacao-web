# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
i = 1
np = int(input('Informe o número de pessoas: '))
while i<=np:
    anterior = atual
    atual = int(input('Instante: '))
    if anterior<=(atual-10):
        total = total + 10
    i += 1
    
print (total)



