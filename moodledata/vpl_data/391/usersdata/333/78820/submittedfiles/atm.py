# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
Valor = int(input('Valor a ser sacado :? ')) 

Cedulas20 = (Valor)//(20)
resto20 = (Valor-(Cedulas20*20))

Cedula10 = (resto20)//(10)
resto10 = (Valor - ((Cedulas20*20)+(Cedulas10*10)))

Cedulas5 = (resto10)//(5)
resto5 = (Valor - ((Cedulas20*20)+(Cedulas10*10)+(Cedulas5*5)))

Cedulas2 = (resto5)//(2)
resto2 = (Valor - ((Cedulas20*20)+(Cedulas10*10)+(Cedulas5*5)+(Cedulas2*2)))

Cedulas1 = (resto)//(1)

print(Cedulas20)
print(Cedulas10)
print(Cedulas5)
print(Cedulas2)
print(Cedulas1)