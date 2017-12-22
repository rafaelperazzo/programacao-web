# -*- coding: utf-8 -*-
from minha_bib import *
import string
#COMECE AQUI ABAIXO

matriz = [
    ['   ','   ','   '],
    ['   ','   ','   '],
    ['   ','   ','   ']
    ]

print (matriz[0][0] + '|' + matriz[0][1] + '|' + matriz[0][2])
print (matriz[1][0] + '|' + matriz[1][1] + '|' + matriz[1][2])
print (matriz[2][0] + '|' + matriz[2][1] + '|' + matriz[2][2])

while true:
    n = input('digite')
    print (n)
    print(n[0])
    print(n[2])
    
    matriz[int(n[0])][int(n[2])] = ' X '
    
    print (matriz[0][0] + '|' + matriz[0][1] + '|' + matriz[0][2])
    print (matriz[1][0] + '|' + matriz[1][1] + '|' + matriz[1][2])
    print (matriz[2][0] + '|' + matriz[2][1] + '|' + matriz[2][2])

    if matriz == [
    [' X ',' X ',' X '],
    [' X ',' X ',' X '],
    [' X ',' X ',' X ']
    ]

