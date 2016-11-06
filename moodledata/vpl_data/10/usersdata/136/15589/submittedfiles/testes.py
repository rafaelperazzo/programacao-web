# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n = input("digite:")
a = []
for i in range (0, n, 1):
    a.append(input("Digite um valor:"))
for i in range (0, n, 1):
    if a[i]%2 ==0:
        print (a[n-1]%2)