# -*- coding: utf-8 -*-
from __future__ import division

i=int(input('digite o valor do investimento :'))
taxa=float(input('digite valor da taxa :'))
t=taxa/100
a1=i+(t*i)
print('lucros em 1 ano :%.2f'%a1)
a2=a1+(t*a1)
print('lucros em 2 anos :%.2f'%a2)
a3=a2+(t*a2)
print('lucros em 3 anos :%.2f'%a3)
