# -*- coding: utf-8 -*-
"""

Created on Mon Aug 29 20:05:07 2016

@author: Jonathan Moreira
"""

from __future__ import division
#ENTRADA

P=input('Digite o valor de P:')
i=input('Digite o valor de i:')
n=input('Digite o valor de n:')

#PROCESSAMENTO

v=(P*(((1.00+i)**n)-1)/float(i))

#SAIDA

print('O valor de v é %.2f' % v)