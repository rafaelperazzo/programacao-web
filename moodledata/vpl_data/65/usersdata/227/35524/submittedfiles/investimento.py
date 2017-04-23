# -*- coding: utf-8 -*-
from __future__ import division

invest=float(input('faça um investimento:'))
taxa=float(input('digite a taxa:'))

investimento=(invest+taxa*invest)

print('%.2f'%investimento)