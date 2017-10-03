# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
s = int(input("Digite o valor a ser sacado: "))
cedula20=s/20
cedula10=(s%20)/10
cedula5=(s%20)/5
cedula2=(s%20)/2
cedula1=(cedula2%2)
print(int(cedula20))
print(int(cedula10))
print(int(cedula5))
print(int(cedula2))
print(int(cedula1))