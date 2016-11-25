# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:15:08 2016

@author: Jonathan Moreira
"""

from __future__ import division
import funcoes
#COMECE AQUI
m=input('Digite m: ')
e=input('Digite epsilon:  ')

print('%.15f' %(funcoes.calcula_pi(m)))
print('%.15f' %(funcoes.calcula_razao_aurea(m,e)))