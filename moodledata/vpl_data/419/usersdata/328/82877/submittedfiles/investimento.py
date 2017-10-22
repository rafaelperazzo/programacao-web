# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento=float(input('Digite o valor investido:'))
t= float(input('Digite a taxa como número:'))
i=0
while(i<=10):
    investimento=investimento+investimento*t
    i=i+1