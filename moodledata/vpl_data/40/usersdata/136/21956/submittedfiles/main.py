# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI


m = input("Digite o número m de termos da fórmula de pi:")
epsilon = input("Digite o epsilon para o calculo da razao aurea:")

print ("Valor aproximado de pi: %.15f" %funcoes.calcula_pi(m))
print ("Valor aproximado da razao aurea: %.15f" %funcoes.calcula_razao_aurea(m, epsilon))