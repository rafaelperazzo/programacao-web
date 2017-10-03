# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
s = int(input("Digite o valor a ser sacado: "))
cedula20=s/20
cedula10=(s%20)/10
cedula5=(cedula10%5)
print(int(cedula20))
print(int(cedula10))
print(int(cedula5))