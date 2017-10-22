# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i = float(input('i: '))
t = float(input('t: '))

for f in range (0,10,1):
    f += (i + (t*i))
    print('%.2f' %f)
    
