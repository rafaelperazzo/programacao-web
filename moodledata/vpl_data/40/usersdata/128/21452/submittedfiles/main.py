# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI


m=input('Digite o número m de termos da fórmula de pi: ')

pi=funcoes.pi(m)
print ('%.15f' %pi)

epsilon=input('Digite o epsilon para o cálculo da razão áurea: ')
razao=funcoes.razaoAurea(m,epsilon)
print ('%.15f' %razao)
