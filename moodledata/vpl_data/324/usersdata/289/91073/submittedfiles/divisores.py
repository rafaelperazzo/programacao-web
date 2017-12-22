# -*- coding: utf-8 -*-
import math
n = int(input("Digite a quantidade de múltiplos: "))
a = int(input("Digite um número inteiro positivo:"))
b = int(input("Digite um número inteiro positivo: "))
mult=1
i=0
while i<n:
    if mult%a==0 or mult%b==0:
        print(mult)
        i=i+1
    mult=mult+1
