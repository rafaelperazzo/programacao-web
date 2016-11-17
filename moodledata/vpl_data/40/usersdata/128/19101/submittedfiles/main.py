# -*- coding: utf-8 -*-
from __future__ import division
import funcoes.pi
import funcoes.cosseno
import funcoes.fatorial

#COMECE AQUI


m=input('Digite o número m de termos da fórmula de pi: ')

print ('%.15f' %funcoes.pi(m))

e=input('Digite o epsilon para o calculo da razão aurea: ')

x=funcoes.pi(m)/5

print ('%.15f' %(2*funcoes.cosseno(x,e)))
