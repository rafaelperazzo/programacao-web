# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#entrada
m = input ('Digite um valor para m:')
e = input ('Digite um valor para e:')

#importando as funções da biblioteca
pi = funcoes.calculapi(m)
RA = funcoes.razaoaurea(m,e)

#saída
print('%.15f' %pi)
print('%.15f' %RA)