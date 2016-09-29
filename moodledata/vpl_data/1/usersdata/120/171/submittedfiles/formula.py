# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
p=input('insira o valor de p:')
i=input('insira o valor de i:')
n=input('insira o valor de n:')
#PROCESSAMENTO
v=p*(((1+i)**n)-1)/i
#SAIDA
print ('%.2f' % v)
