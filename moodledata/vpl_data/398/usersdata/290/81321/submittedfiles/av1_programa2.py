# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
b=int

a=int(input("Primeira carta: "))
b=int(input("Segunda carta: "))
c=int(input("Terceira carta: "))
d=int(input("Quarta carta: "))
e=int(input("Quinta carta: "))
f=int(input("Sexta carta: "))
if a<b and b<c and c<d and d<e and e<f:
    print("C")
elif f>e and e>d and d>c and c>b and b>a:
    print("D")
else:
    print("N")