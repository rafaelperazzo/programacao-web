# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
#i = float(input('i: '))
#t = float(input('t: '))
i = 1000
t = 0.045
#z = (i + (t*i))
for f in range (10):
    f += (i + (t*i))
    print('%.2f' %f)
    
