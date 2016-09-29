# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
p1 =input('Qual o peso da criança do lado esquerdo?')
c1 =input('Qual o comprimento da gangorra do lado esquerdo?')
p2 =input('Qual o peso da criança do lado direito?')
c2 =input('Qual o comprimento da gangorra do lado direito?')

#PROCESSAMENTO
lDireito = p2*c2
lEsquerdo = p1*c1
if lDireito==lEsquerdo:
    print('0')
elif lDireito>lEsquerdo:
    print('1')
elif lEsquerdo>lDireito:
    print('-1')

