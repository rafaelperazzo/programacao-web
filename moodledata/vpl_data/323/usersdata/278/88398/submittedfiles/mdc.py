# -*- coding: utf-8 -*-
import math
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
if n1>n2:
    resto = n1%n2
    while (resto>0):
        resto_ = n2/resto
        n2=resto
        resto=resto_
    
