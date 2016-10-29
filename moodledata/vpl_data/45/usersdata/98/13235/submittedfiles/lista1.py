# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite o valor de n: ')
somaI=0
somaP=0
contI=0
contP=0

for i in range (1,n+1,1):
    v=input('Digite um valor: ')
    if v%2==1:
        somaI=somaI+v
        contI=contI+1
    if v%2==0:
        somaP=somaP+v
        contP=contP+1
