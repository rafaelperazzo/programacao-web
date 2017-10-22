# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento=float(input("investimento inicial:"))
taxa=float(input("taxa de juros:"))
ano=0
while ano<10:
    investimento=(investimento+taxa*investimento)
    ano=ano+1
    print(" %.2f"%(investimento))
    