# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i= int(input('Digite o valor do investimento: '))
t= float(input('Digite o valor da taxa: '))
for valor in range (0,10,(i+t*i)):
    print (valor)