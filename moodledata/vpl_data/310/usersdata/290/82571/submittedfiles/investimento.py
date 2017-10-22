# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v=float(input("Digite o valor do invertimento: "))
t=float(input("Digite a taxa de crescimento: "))
va=(v+(v*t))
i=1
while (i<11):
    print("%.2f"%va)
    i+=1
    va=(va+va*t)

    