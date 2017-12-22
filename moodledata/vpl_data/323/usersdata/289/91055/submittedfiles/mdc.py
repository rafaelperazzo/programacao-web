# -*- coding: utf-8 -*-
import math
n1=int(input("Digite um número inteiro positivo: "))
n2=int(input("Digite um número inteiro positivo: "))
resto = n1%n2
while (resto!=0):
    n1=n2
    n2=resto
    resto=n1%n2
    print(n2)