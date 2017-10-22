# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
#ENTRADA
i= float(input('Digite valor do investimento inicial i: '))
t= float(input('Digite valor de taxa t: '))
v=i+(i*t)
c=1
while(c<11):
    print('%.2f' %v)
    v=v+(v*t)
    c=c+1

