# -*- coding: utf-8 -*-
from __future__ import division
import funcoes as fu

m=input("Digite o numero m de termos da formula para pi: ")
ep=input("Digite o epsilon para o calculo da razao aurea: ")
print
print "Valor aproximado de pi: %.15f"%(fu.cpi(m))
print "Valor aproximado da razao aurea %.15f"%(fu.cra(m,ep))

