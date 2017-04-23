# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
Valor=float(input("Digite o valor de investimento: "))
Taxa=float(input("Digite o valor da taxa:"))
t=1
while t <= 10:
    Total=Valor*((1+Taxa)**t)
    print("%.2f" %Total)
    t=t+1