# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
#ENTRADA
x = int(input('Digite o valor em dinheiro: '))
b = x//20
b1 = x%20
#PROCESSAMENTO
c1 = (b1//10)
d2 = (c1%10)
d1 = (d2//5)
e2 = (d1%5)
e1 = (e2//2)
f2 = (e1%2)
f1 = (e1//1)
#SAIDA
print(b)
print(c1)
print(d1)
print(e1)
print(f1)
