# -*- coding: utf-8 -*-
from __future__ import division
import math

Valor = int(input('Digite o valor a ser sacado:'))

Cedula20 = int(Valor/20)
RestodaCedula20 = (Valor - (Cedula20 * 20))
Cedula10 = int(RestodaCedula20/10)
RestodaCedula10 = (RestodaCedula20 - (Cedula10 *10))
Cedula5 = int(RestodaCedula/5)
RestodaCedula5 = (RestodaCedula10 - (Cedula5 *5))
Cedula2 = int(RestodaCedula5/2)
RestodaCedula2 = (RestodaCedula5 - (Cedula2 * 2))
Cedula1 = int(RestodaCedula2/1)
RestodaCedula1 = (RestodaCedula2 - (Cedula1 * 1))

print Cedula20
print Cedula10
print Cedula5
print Cedula2
print Cedula1