# -*- coding: utf-8 -*-
from __future__ import division
import funcoes


m=input('Digite o numero m de termos da formula de pi:')  
e=input('Digite o epsilon para o calculo da razao aurea:')
valorpi= pi(m)
x=(pi(m)/5)
razao=RazaoAurea(x,e)
print ('Valor aproximado de pi:%.15f'%valorpi)
print ('Valor aproximado da razao aurea:%.15f'%razao)