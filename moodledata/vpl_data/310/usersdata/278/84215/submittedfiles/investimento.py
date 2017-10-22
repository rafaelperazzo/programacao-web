# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
c = float(input("Digite o valor do investimento inicial: " ))
i = float(input("Digite a taxa de crescimento percentual [0,1]: "))
t=1
while (t<=10):
    total = (c*i*t)+c
    print(total)
    t=+1