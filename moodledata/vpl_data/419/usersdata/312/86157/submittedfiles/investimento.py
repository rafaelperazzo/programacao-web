# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento=float(input("deposito inicial:"))
taxa=float(input("taxa de juros:"))
ano=1
soma=0
while ano<11:
    investimento=(investimento+taxa*investimento)
    print(" %.2f"%(investimento))
    