# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento=float(input("deposito inicial:"))
taxa=float(input("taxa de juros:"))
ano=1
soma=0
while ano<10:
    investimento=(investimento+taxa*investimento)
    print(ano)
    ano=ano+1
    somo=soma+investimento
    print("o redimento do ano é %d é de %5.2f"%(investimento))
