# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite a quantidade de salas:')
vidas = input('Digite a quantidade de vidas de cada sala:')
entrada = input('Digite a porta de entrada:')
saida = input('Digite a porta de saida:')

resultado = ((saida - entrada) + 2)*vidas

print('%.d' %resultado)