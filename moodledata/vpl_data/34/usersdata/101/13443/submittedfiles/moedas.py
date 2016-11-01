# -*- coding: utf-8 -*-
from __future__ import division

a = int(input('digite o valor da moeda a: '))
b = int(input('digite o valor da moeda b: '))
c = int(input('digite o valor da moeda c: '))

troca = False
na = 0

while c//a >= na and not troca: 
    nb = 0
    while c//b >= nb and not troca:
        if na*a + nb*b == c:
            troca = True
        nb += 1
    na += 1
    
if troca:
    print ('%d moedas de %d e %d moedas de %d' %(na-1, a, nb-1, b))
else:
    print ('Não é possível trocar a cédula')