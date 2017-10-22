# -*- coding: utf-8 -*-
import math
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
if n1>n2:
    resto = n1%n2
    while (resto>0):
        n1=n2
        n2=resto
        resto = n2%resto
    print(n2)
if n2>n1:
    resto = n2%n1
    while (resto>0):
        n2=n1
        n1=resto
        resto = n1%resto
    print(n1)
if n1==n2:
    print(n1)
            
    
    
