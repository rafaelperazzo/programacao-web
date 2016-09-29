# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA

n = input('Digite a quantidade de lados do polígono: ')

#PROCESSAMENTO

nd = float((n*(n - 3))/2)

#SAÍDA

print "O número de diagonais diferentes é: " + str(nd)