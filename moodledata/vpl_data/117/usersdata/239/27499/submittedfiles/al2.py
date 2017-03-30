# -*- coding: utf-8 -*-
#Separar a parte inteira de um número e a parte fracionária, ex 5.39568, parte inteira 5, fracionaria 0.39568
print("Separador de inteiros e fracionários")
print("")
A = float(input("Digite o número: "))
B = int(A)
C = A-B
print("A parte Inteira é: %f"%B)
print("A parte fracionária é: %f"%C) 