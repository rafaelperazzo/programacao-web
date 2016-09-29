# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v=input('Digite o valor do investimento:')
taxa=input('Digite o valor da taxa anual:')

m1=(v+(taxa*v))
m2=(m1+(taxa*m1))
m3=(m2+(taxa*m2))
m4=(m3+(taxa*m3))
m5=(m4+(taxa*m4))
m6=(m5+(taxa*m5))
m7=(m6+(taxa*m6))
m8=(m7+(taxa*m7))
m9=(m8+(taxa*m8))
m10=(m9+(taxa*m9))


print('%.2f'%m1)
print('%.2f'%m2)
print('%.2f'%m3)
print('%.2f'%m4)
print('%.2f'%m5)
print('%.2f'%m6)
print('%.2f'%m7)
print('%.2f'%m8)
print('%.2f'%m9)
print('%.2f'%m10)


