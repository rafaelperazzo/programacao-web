# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v=input('Valor do investimento inicial:')
t=input('Taxa de crescimento percentual:')

i1=v+(t*v)
i2=i1+(t*i1)
i3=v+(t*i2)
i4=v+(t*i3)
i5=v+(t*i4)
i6=v+(t*i5)
i7=v+(t*i6)
i8=v+(t*i7)
i9=v+(t*i8)
i10=v+(t*i9)

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

