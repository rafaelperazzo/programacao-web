# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
#i = float(input('i: '))
#t = float(input('t: '))
i = 1000
t = 0.045
cont = 0
while (cont<10):
    i = i + (t*i)
    print('%.2f' %i)
    cont=cont+1

