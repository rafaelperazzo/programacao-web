# -*- coding: utf-8 -*-
from __future__ import division
import funcoes as fu

m=input("Digite o numero m de termos da formula para pi: ")
ep=input("Digite o epsilon para o calculo da razao aurea: ")

pi=fu.cpi(m)
pi5=pi/5.0
aurea=2*fu.ccos(pi5,ep)

print "Valor aproximado de pi: %.15f"%pi
print "Valor aproximado da razao aurea %.15f"%aurea
