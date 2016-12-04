# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

m = input('Digite a quantidade de termos que deseja obter no valor de Pi: ')
eps = input('Digite o valor de epsilon para que realize-se o cálculo da razão auréa: ')


print ('O valor aproximado de pi é: %.15f' %(funcoes.Pi(m))
print ('A razão auréa equivale a aproximadamente %.15f' %(funcoes.RA(m,eps))