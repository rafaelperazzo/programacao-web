# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v=input('Valor do investimento inicial:')
t=input('Taxa de crescimento percentual:')

i1=v+(t*v)
i2=i1+(t*i1)
i3=i2+(t*i2)
i4=i3+(t*i3)
i5=i4+(t*i4)
i6=i5+(t*i5)
i7=i6+(t*i6)
i8=i7+(t*i7)
i9=i8+(t*i8)
i10=i9+(t*i9)

print('%.2f' %i1)
print('%.2f' %i2)
print('%.2f' %i3)
print('%.2f' %i4)
print('%.2f' %i5)
print('%.2f' %i6)
print('%.2f' %i7)
print('%.2f' %i8)
print('%.2f' %i9)
print('%.2f' %i10)

