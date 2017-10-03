# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
a=int(input("Digite um número: "))
b=int(input("Digite um número: "))
c=int(input("Digite um número: "))
d=int(input("Digite um número: "))
e=int(input("Digite um número: "))
f=int(input("Digite um número: "))

if a>b and b>c and c>d and d>e and e>f:
    print("D")
elif a<b and b<c and c<d and d<e and e<f:
    print("C")
else:
    print("N")