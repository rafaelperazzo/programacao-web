# -*- coding: utf-8 -*-
from __future__ import division
import math
n =  input ('digite o intevalo:')
a =  input ('digite o valor 1:')
b =  input ('digite o valor 2:')

contador = 1
i=1
while contador <=n:
    if i%a==0 or i%b==0:
        print i
        contador = contador +1
    i=i+1
