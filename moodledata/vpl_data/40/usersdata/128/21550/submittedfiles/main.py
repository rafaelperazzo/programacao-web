# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI


m=input('Digite o número m de termos da fórmula de pi: ')

print ('%.15f' %funcoes.pi(m))

epsilon=input('Digite o epsilon para o cálculo da razão áurea: ')

print ('%.15f' %funcoes.razaoAurea(m,epsilon))
