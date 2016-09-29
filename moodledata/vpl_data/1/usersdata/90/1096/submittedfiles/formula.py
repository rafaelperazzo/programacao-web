# -*- coding: utf-8 -*-
from __future__ import division
#entrada
p=input('Digite aqui o valor de p:')
i=input('Digite aqui o valor de i:')
n=input('Digite aqui o valor de n:')

#processamento
v=p*(((1+i)**n)-1)/i

#saida
print ('O resultado é:%2.f'%(v))
