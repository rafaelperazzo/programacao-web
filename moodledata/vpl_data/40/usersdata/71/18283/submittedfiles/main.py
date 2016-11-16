# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

print funcoes.razao_aurea(100,0.0001)

m = input("Digite o numero m de termos da formula de pi: ")
epsilon = input("Digite o epsilon para o calculo da razao aurea: ")
print ("Valor aproximado de pi: %.15f" %pi(m))
print("Valor aproximado da razao aurea: %.15f" %razao_aurea(m,epsilon))