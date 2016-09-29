# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
#Entrada
c = input('Digite o valor que você quer sacar:')

#Processamento
a20 = c//20
a10 = (c-(a20*20))//10
a5 = (c-((a20*20)+(a10*10)))//5
a2 = (c-((a20*20)+(a10*10)+(a5*5)))//2
a1 = c-((a20*20)+(a10*10)+(a5*5)+(a2*2))

#Saída
print a20
print a10
print a5
print a2
print a1

