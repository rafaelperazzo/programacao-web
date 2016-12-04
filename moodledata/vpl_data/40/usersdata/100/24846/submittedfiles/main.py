# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m = input("Digite o numero m de termos da formula do Pi: ")
epsilon = input("Digite o epsilon para o calculo da razao aurea: ")
print ("Valor aproximado de Pi: %.15f" %funcoes.calcula_pi(m))
print("Valor aproximado da Razao Áurea: %.15f" %funcoes.calcula_razao_aurea(m,epsilon))