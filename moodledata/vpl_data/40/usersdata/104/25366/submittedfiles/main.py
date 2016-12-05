# -*- coding: utf-8 -*-
from __future__ import division
import funcoes
m=input('Digite o numero de m termos da formula de pi:')
epsilon=input('Digite o epsilon para o calculo da razao aurea:')

pi=funcoes.calcula_pi(m)
razao=funcoes.calcula_razao_aurea(m,epsilon)

print('%.15f'%(pi))


