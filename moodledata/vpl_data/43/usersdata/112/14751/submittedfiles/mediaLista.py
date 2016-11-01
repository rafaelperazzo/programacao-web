# -*- coding: utf-8 -*-
from __future__ import division

soma=0
mitocondria=input('Digite a quantidade de números:')
jutsu=[]
for i in range (0,mitocondria,1):
    jutsu.append(input('e aêêêêêÊ:'))
for a in range (0,mitocondria,1):
    soma=(soma+jutsu[a])

print('%.2f'%jutsu[0])
print('%.2f'%jutsu[mitocondria-1])
print('%.2f'%(soma/mitocondria))
print(jutsu)
        