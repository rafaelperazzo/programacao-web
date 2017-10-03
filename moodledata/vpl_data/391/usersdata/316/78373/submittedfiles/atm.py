# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
s = int(input("Digite o valor a ser sacado: "))
cedula20=s/20
cedula10=(s-(20*cedula20))/10
print(int(cedula20))
print(int(cedula10))