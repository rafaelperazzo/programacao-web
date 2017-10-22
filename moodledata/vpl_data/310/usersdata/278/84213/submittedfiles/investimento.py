# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
ii = float(input("Digite o valor do investimento inicial: " ))
cp = float(input("Digite a taxa de crescimento percentual [0,1]: "))
t=1
while (t<=10):
    total = ii*(1+cp)*t
    print(total)
    t=+1