# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i = float(input('i: '))
t = float(input('t: '))
z = (i + (t*i))
for f in range (0,10,1):
    f += z
    print('%.2f' %f)
    
