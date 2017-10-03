# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
import math

i = 2.0
j = 1.0
auxi = 2.0
auxj = 1.0
cont = 0


n = int(input(''))

while n>0:
    n = n - 1
    
    j = j * auxj
    i = i * auxi

    
    if cont == 0:
        auxj = auxj + 2
        cont = cont + 1
    else: 
        auxi = auxi + 2
        cont = cont - 1

pi = i/j
mathisnan(pi)

print('%.5f' %pi)