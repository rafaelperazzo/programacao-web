# -*- coding: utf-8 -*-
import math
n1=int(input("Digite o 1º número: "))
n2=int(input("Digite o 2º número: "))
n3=int(input("Digite o 3º número: "))
n4=int(input("Digite o 4º número: "))
cont=0
if n1>n2:
    cont=cont + 1
if n2>n3 and n2>n1:
    cont=cont + 1
if n3>n4 and n3>n2:
    cont=cont + 1
if n4>n3:
    cont=cont + 1
if cont == 1:
    print("S")
if cont != 1:
    print("N")