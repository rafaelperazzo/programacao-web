# -*- coding: utf-8 -*-
#COMECE A PARTIR DAQUI!
x1 = int(input('Digite o valor de x1: '))
x2 = int(input('Digite o valor de x2: '))
SOMA = 0
while (x1 < x2):
    if x1%2 == 0 :
        SOMA += x1
    x1 += 1
print(SOMA)    
    