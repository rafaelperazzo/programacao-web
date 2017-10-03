# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
'''Exercício 1 proposto pela monitoria
i = 1
atual = 0
total = 0
limanterior = 0
np = int(input('Informe o número de pessoas: '))
while i<=np:
    atual = int(input('Instante: '))
    total = total+10
    if atual<(limanterior):
        total = total - (limanterior - atual)
    limanterior = atual +10
    i += 1
print (total)



