# -*- coding: utf-8 -*-
from minha_bib import *
#COMECE AQUI ABAIXO
matriz['0 0'] = 'X'
matriz = [
    ['   ','   ','   '],
    ['   ','   ','   '],
    ['   ','   ','   ']
    ]

print (matriz['0 0'] + '|' + matriz[0][1] + '|' + matriz[0][2])
print (matriz[1][0] + '|' + matriz[1][1] + '|' + matriz[1][2])
print (matriz[2][0] + '|' + matriz[2][1] + '|' + matriz[2][2])



for i in range (0,9,1):
    for j in range (0,9,1):
       matriz[j] = 1


