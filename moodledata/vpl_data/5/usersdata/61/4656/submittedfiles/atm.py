# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
V=int(input('Digite um valor a ser sacado: '))
cedula20=int(V/20)
resto1=(V-(cedula20*20))
cedula10=int(resto1/10)
resto2=(resto1-(cedula10*10))
cedula5=int(resto2/5)
resto3=(resto2-(cedula5*5))
cedula2=int(resto3/2)
resto4=(resto3-(cedula2*2))
cedula1=int(resto4/1)
resto5=(resto4-(cedula1*2))
print cedula20
print cedula10
print cedula5
print cedula2
print cedula1




