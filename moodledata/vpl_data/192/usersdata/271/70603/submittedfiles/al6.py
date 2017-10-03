# -*- coding: utf-8 -*-
#ENTRADA
n = int(input('Digite o valor de n : '))
#PROCESSAMENTO
i = 2
contador = 0
while (i<n) :
    if (n%i) == 0 :
        contador = contador+1
    i = i+1
if contador == 0 :
    print '
        