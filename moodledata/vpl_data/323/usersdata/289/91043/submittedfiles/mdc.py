# -*- coding: utf-8 -*-
import math
n1=int(input("Digite um número inteiro positivo: "))
n2=int(input("Digite um número inteiro positivo: "))
i=1
while (n1%i==0 and n2%i==0):
    print(i)
    i += 1