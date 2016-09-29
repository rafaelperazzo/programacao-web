# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i = input ('Digite o valor inicial do investimento:')
t = input ('Digite a taxa de correção anual:')


v1 = i+t*i
v2 = v1+t*v1
v3 = v2+t*v2
v4 = v3+t*v3
v5 = v4+t*v4
v6 = v5+t*v5
v7 = v6+t*v6
v8 = v7+t*v7
v9 = v8+t*v8
v10 = v9+t*v9

print ('%.2f'%v1)
print ('%.2f'%v2)
print ('%.2f'%v3)
print ('%.2f'%v4)
print ('%.2f'%v5)
print ('%.2f'%v6)
print ('%.2f'%v7)
print ('%.2f'%v8)
print ('%.2f'%v9)
print ('%.2f'%v10)

