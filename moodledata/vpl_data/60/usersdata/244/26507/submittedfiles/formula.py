# -*- coding: utf-8 -*-

p = float(input('Digite o valor p:'))
i = float(input('Digite o valor i:'))
n = float(input('Digite o valor n:'))

v = p *((((1+i)**n)-1)/i)

print('%.2f' % v)
