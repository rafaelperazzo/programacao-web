# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
s=int(input('Digite s: '))
e=input('Digite epsilon: ')

mod=funcoes.modulo(s)

PI=funcoes.pi(s)

Coss=funcoes.cosseno(PI/5,e)

RazaoA=funcoes.RA(s,e)

print ('%.15f' %PI)
print ('%.15f' %RazaoA)

