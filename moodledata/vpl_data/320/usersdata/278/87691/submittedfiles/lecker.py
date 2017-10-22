# -*- coding: utf-8 -*-
import math
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
t=0
if n1>n2:
    t+=1
if n1<n2 and n2>n3:
    t+=1
if n2<n3 and n3>n4:
    t+=1
if n3<n4:
    t+=1
if t>1:
    print("N")
if t=1:
    print("S")