# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import math
x = input ('valor incial')
e = x
#calculo newtoniano
while (e >= str(0.001)):
    f = (math.sin(x) - x**4)
    g = math.cos(x) - 4*(x**3)
    q = x
    x = q - f/g
    e = np.abs(x-q)
print (x)