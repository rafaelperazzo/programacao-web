# -*- coding: utf-8 -*-
n = float(input("Digite o valor de n: "))
contador = 0
while (n>0):
    n = n//10
    contador = contador+1
print (contador)