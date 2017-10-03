# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor = int(input('Valor a ser sacado'))
cedulas20 = (valor//20)
resto20 = (valor - (cedulas20*20))
cedulas10 = resto20//10
resto10 = (resto20 - (cedulas10*10))
cedulas5 = (resto10//5)
resto5 = (resto10 - (cedulas5*2))
cedulas2 = (resto5//2)
resto2 = (resto5 - (cedulas2*2)
cedulas1 = (resto2//1)
print(cedulas20)
print(cedulas10)
print(cedulas5)
print(cedulas2)
print(cedulas1)