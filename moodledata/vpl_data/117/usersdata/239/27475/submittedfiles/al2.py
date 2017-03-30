# -*- coding: utf-8 -*-
#Separar a parte inteira de um número e a parte fracionária, ex 5.39568, parte inteira 5, fracionaria 0.39568
print("Separador de inteiros e fracionários")
print("")
A = float(input("Digite o número: "))
B = int(input(A))
C = float(input(A-B))
print("A parte Inteira é: "%A)
print("A parte fracionária é: "%B) 