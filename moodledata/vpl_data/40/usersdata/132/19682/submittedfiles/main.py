# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
m=input('digite o numero m de termos da formula do pi:')
c=funcoes.pi(m)#import da função pi para o programa principal
print('o valor do pi é %.15f'%c)
e=input('digite o valor de epsilon para o calculo da razao aurea:')
a=funcoes.aurea(m,e)#import da função áurea para o programa principal
print('o valor da razao aurea para suas entradas e %.15f'%a)