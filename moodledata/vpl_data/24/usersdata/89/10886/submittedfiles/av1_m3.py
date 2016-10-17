# -*- coding: utf-8 -*-
from __future__ import division
import math
#entrada
m=input('digite o valor de m:')
#processamento e saida
termo=1
denominador=2
soma=0
while termo<=m:
    if termo%2==0:
        soma=soma-(4/(denominador)*(denominador)*(denominador))
    else:
        soma=soma+(4/(denominador)*(denominador)*(denominador))
