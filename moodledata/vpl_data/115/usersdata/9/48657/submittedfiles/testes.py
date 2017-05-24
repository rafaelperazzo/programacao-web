# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import math
x = float(input ('valor incial'))
e = float(x)
k = float(0.001)
#calculo newtoniano
while (e>=k):
    f = math.sin(x) - x**4
    g = math.cos(x) - 4*(x**3)
    q = x
    x = q - f/g
    e = np.abs(q-x)
    print(x)
print (x)