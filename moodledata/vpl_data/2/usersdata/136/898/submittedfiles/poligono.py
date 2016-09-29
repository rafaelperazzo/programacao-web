# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
n = input("Digite o número de lados do polígono:")
#PROCESSAMENTO
nd = (n*(n-3))/2
#SAIDA
print("O número de diagonais diferentes, desse polígono é %.2f" %nd)