# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#ÁREA DESTINADA A ENTRADA E SAÍDA DO TRABALHO.
#ONDE VAI SER INSERIDO OS VALORES DOS TERMOS PRESENTES NA FORMULA DE PI, E O VALOR DE EPSILON.



#ENTRADA
m=input('Digite o numero de termos m da formula de pi:')
e=input('Digite o valor de epsilon para o calculo da razao aurea:')



#SAÍDA
print('O Valor aproximado de pi:%.15f'%(funcoes.calcula_pi(m)))
print('O Valor aproximado da razao aurea:%.15f'%(funcoes.calcula_razao_aurea(m,e)))
