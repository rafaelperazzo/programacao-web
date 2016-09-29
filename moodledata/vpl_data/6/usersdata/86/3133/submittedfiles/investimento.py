# -*- coding: utf-8 -*-
from __future__ import division

#entrada
vii = input('digite o valor de investimento inicial:')
tcp = input('digite o valor da taxa de crescimento percentual:')
#processamento
investimento1 = vii+vii*tcp
investimento2 = investimento1+investimento1*tcp
investimento3 = investimento2+investimento2*tcp
investimento4 = investimento3+investimento3*tcp
investimento5 = investimento4+investimento4*tcp
investimento6 = investimento5+investimento5*tcp
investimento7 = investimento6+investimento6*tcp
investimento8 = investimento7+investimento7*tcp
investimento9 = investimento8+investimento8*tcp
investimento10 = investimento9+investimento9*tcp
#saida
print('%.2f'%investimento1)
print('%.2f'%investimento2)
print('%.2f'%investimento3)
print('%.2f'%investimento4)
print('%.2f'%investimento5)
print('%.2f'%investimento6)
print('%.2f'%investimento7)
print('%.2f'%investimento8)
print('%.2f'%investimento9)
print('%.2f'%investimento10)

