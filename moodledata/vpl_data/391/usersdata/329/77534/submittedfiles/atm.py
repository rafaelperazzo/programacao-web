# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor = int(input('digite o valor= '))
cedulas=0
valorcedulaatual=20
valoraserentregue=valor
while True:
    if valorcedulaatual<=valoraserentregue:
        cedulas += 1
        valoraserentregue -= valorcedulaatual
    else:
        print("%.1d" % (cedulas, valorcedulaatual))
        if valoraserentregue == 0:
            break
        if valorcedulaatual == 20:
            valorcedulaatual = 10
        elif valorcedulaatual == 10:
            valorcedulaatual = 5
        elif valorcedulaatual == 5:
            valorcedulaatual = 2
        elif valorcedulaatual == 2:
            valorcedulaatual = 1
        cedulas=0
    
        