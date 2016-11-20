# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

m=int(input('Digite m:'))
e=input('Digite o epsilon para o cosseno:')


pi = funcoes.calcula_pi (m)
razao_aurea = funcoes.calcula_razao_aurea (m,e)

print('%.15f' %pi)
print('%.15f' %razao_aurea)
