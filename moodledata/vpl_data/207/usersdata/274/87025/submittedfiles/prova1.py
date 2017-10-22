# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
#ENTRADA
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))
d = int(input("Quarto número: "))
e = int(input("Quinto número: "))
#PROCESSAMENTO E SAIDA
if (a>b) and (b>c) and (c>d) and (d>e):
    print("D")
elif (a<b) and (b<c) and (c<d) and (d<e):
    print("C")
else:
    print ("N")
