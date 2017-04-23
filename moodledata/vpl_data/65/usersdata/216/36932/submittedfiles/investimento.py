# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v=float(input('Digite o vslor inicial do investimento:'))
t=float(input('Digite a taxa percentual:'))

t1=v+(v*t)
t2=t1+(t1*t)

print('%.2f'%t1)
print('%.2f'%t2)