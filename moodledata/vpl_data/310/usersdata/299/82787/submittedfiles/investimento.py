# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v=float(input(''))
t=float(input(''))
for i in range(10):
    v=v+v*t
    print('%.2f' %v)