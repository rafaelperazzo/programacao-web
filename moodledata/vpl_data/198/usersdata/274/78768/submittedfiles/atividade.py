# -*- coding: utf-8 -*-
n = int(Input("Digite o valor de n: "))
contador = 0
while (n>=1):
    n = n//10
    contador = contador+1
print (contador)