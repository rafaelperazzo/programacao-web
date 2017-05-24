# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import math
x = input ('valor incial')
e = x
#calculo newtoniano
while (str(e)>=float(0.001)):
    f1 = (float(math.sin(x)) - float(x**4))
    f2 = math.cos(x) - 4*(x**3)
    q = x
    x = q - f1/f2
    e = np.abs(x-q)
print (x)