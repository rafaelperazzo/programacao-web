# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m = input ('Digite um valor para m:')
e = input ('Digite um valor para e:')

pi = funcoes.calculapi(m)
RA = funcoes.razaoaurea(m,e)
print('%.15f' %pi)
print('%.15f' %RA)