# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO AQUI
P = int(input('Insira a posição da Porta P: '))
R = int(input('Insira a posição da Porta R: '))

#processamento
if P==0:
    print('C')
if P==1:
    if R==0:
        print('B')
    if R==1:
        print('A')
    else:
        print('Entrada Inválida')
else:
    print('Entrada Inválida')