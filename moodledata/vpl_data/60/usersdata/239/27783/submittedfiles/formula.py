# -*- coding: utf-8 -*-
print("Reolução do exercício 3")
print("OBS. O valor de i tem que ser diferente de 0")
print("")
P = float(input("Digite o valor de P.: "))#Declarando P
i = float(input("Digite o valor de i.: "))#Declarando i
n = float(input("Digite o valor de n.: "))#Declarando n
v = (P*((1+i)**n)-1)/i #i tem que ser diferente de 0 (zero), condição para calcular.
print("")
print("O valor de v é.: %.2f"%v)

