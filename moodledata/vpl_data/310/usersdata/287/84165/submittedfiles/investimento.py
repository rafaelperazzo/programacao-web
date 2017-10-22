# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

invest=float(input('digite o valor do seu investimento: '))
taxa=float(input('digite o valor da taxa de crescimento anual em decimal: '))
ano=1
while ano<=10:
    invest=invest+(taxa*invest)
    print('%.2f'%(invest))
    ano+=1
    
