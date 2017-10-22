# -*- coding: utf-8 -*-
#ENTRADA
n = int(input('Digite o valor de um numero : '))
bin = 0
i = 0
#PROCESSAMENTO
while (n>0) :
    bin = bin + (n%2) * (10**i)
    i = i+1
    n = n//10
    



