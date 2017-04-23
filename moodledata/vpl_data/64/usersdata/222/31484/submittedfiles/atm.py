# -*- coding: utf-8 -*-
from __future__ import division
import math

valor= float(input('Digite o valor a ser sacado:'))
cedulas=0
valorcedulaatual=0
valoraserentregue=valor
while true:
    if valorcedulaatual <= valor:
        cedula += 1
        valoraserentregue -= valorcedulaatual
    else:
       print('%d cedula(s) de R$ %.2f' % (cedulas, valorcedulaatual))
