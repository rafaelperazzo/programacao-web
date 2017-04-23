# -*- coding: utf-8 -*-
from __future__ import division
import math

valor= int(input('Digite o valor a ser sacado:'))
cedulas=0
valorcedulaatual=0
valoraserentregue=valor
while:
    if valorcedulaatual <= valor:
        cedula += 1
        valoraserentregue -= valorcedulaatual
   else:
       print('%d cedula(s) de R$ $d'(cedulas, valorcedulaatual))
