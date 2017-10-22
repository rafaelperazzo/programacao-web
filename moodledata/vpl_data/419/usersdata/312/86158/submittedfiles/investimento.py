# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento=float(input("deposito inicial:"))
taxa=float(input("taxa de juros:"))
ano=1
while ano<11:
    investimento=(investimento+taxa*investimento)
    ano=ano+1
    print(" %.2f"%(investimento))
    