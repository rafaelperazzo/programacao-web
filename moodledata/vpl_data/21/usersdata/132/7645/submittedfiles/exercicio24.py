# -*- coding: utf-8 -*-
from __future__ import division
import math
salario=float(input('digite o salario:')
base=salario
imposto=0
if base>3000:
    imposto=imposto+((base-1000)*0.35)
    base=3000
if base>1000:
    imposto=imposto + ((base-1000)*0.2)
print(' salario: %.2f'%(salario, imposto)
