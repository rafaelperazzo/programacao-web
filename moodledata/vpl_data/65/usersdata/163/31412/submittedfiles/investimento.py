# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento=float(input('Digite o investimneto:'))
taxa=float(input('Digite a taxa de crescimento:'))

r1=investimento + taxa * investimento  
r2=taxa*r1+r1 
r3=taxa*r2+r2
r4=taxa*r3+r3
r5=taxa*r4+r4
r6=taxa*r5+r5
r7=taxa*r6+r6
r8=taxa*r7+r7
r9=taxa*r8+r8
r10=taxa*r9+r9

print('%.2f'%r1)
print('%.2f'%r2)
print('%.2f'%r3)
print('%.2f'%r4)
print('%.2f'%r5)
print('%.2f'%r6)
print('%.2f'%r7)
print('%.2f'%r8)
print('%.2f'%r9)
print('%.2f'%r10)

