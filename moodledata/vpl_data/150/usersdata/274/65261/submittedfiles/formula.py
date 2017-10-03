# -*- coding: utf-8 -*-
#ENTRADA
P = float(input("Valor de P: "))
i = float(input("Valor de i: "))
n = float(input("Valor de n: "))
#PROCESSAMENTO
V = (P*((1+i)**n)-1)/i
#SAIDA
print("%.2f" % V)
