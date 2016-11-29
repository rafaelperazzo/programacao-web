# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m=input("Digite o numero m de termos da formula para pi: ")
ep=input("Digite o epsilon para o calculo da razao aurea: ")

pi=cpi(m)
pi5=pi/5.0
aurea=2*ccos(pi5,ep)

print "Valor aproximado de pi: %.15f"%pi
print "Valor aproximado da razao aurea %.15f"%aurea
