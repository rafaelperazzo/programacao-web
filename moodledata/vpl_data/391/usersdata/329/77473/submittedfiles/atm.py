# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor = int(input('digite o valor= '))
cedulas=0
valorcedulaatual=100
valoraserentregue=valor
while True:
    if valorcedulaatual<=valor:
        cedula += 1
        valoraserentregue -= valorcedulaatual
        