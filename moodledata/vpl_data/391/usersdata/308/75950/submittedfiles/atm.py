# -*- coding: utf-8 -*-
from __future__ import division
import math
valor = int(input('Valor: '))
#[20, 10, 5, 2, 1]
notas= [0, 0, 0, 0, 0] 

while valor>0:
    if valor>=20:
        notas[0]+= 1
        valor -= 20
    if 20>valor>=10:
        notas[1]+= 1
        valor -= 10
    if 10>valor>=5:
        notas[2]+= 1
        valor -= 5
    if 5>valor>=2:
        notas[3]+= 1
        valor -= 2
    if 2>valor>=1:
        notas[4]+= 1
        valor -= 1
    
print(notas)
#COMECE SEU CODIGO AQUI
