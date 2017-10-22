# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
vi = int(input("Digite o valor do investimento inicial: "))
t = float(input("Digite o valor da taxa de crescimento percentual: "))
ano = 1
while ano<=10:
    if 0<t<1:
        vi = vi + (vi*t)
        print("%.2f" % vi)
        ano = ano + 1