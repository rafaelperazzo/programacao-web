# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
ii = float(input("Digite o valor do investimento inicial: " ))
cp = float(input("Digite a taxa de crescimento percentual [0,1]: "))
t=1
m=0
while (t<=10):
    total = ii*(1+cp)+m
    print(total)