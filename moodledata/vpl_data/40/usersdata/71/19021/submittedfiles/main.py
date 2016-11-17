# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m = input("Digite o numero m de termos da formula do Pi: ")
epsilon = input("Digite o epsilon para o calculo da razao aurea: ")
print ("Valor aproximado de pi: %.15f" %pi(m))
print("Valor aproximado da razao aurea: %.15f" %funcoes.razao_aurea(m,epsilon))