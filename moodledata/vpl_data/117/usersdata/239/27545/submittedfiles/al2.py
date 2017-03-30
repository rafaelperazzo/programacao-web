# -*- coding: utf-8 -*-
#Separar a parte inteira de um número e a parte fracionária, ex 5.39568, parte inteira 5, fracionaria 0.39568
print("Separador de inteiros e fracionários") #Nome
print("Obs1.: Utilize ponto (.) para separar casas decimais")
print("")
A = float(input("Digite o número: ")) #Declarando o valor a ser separado
print("")
B = int(A) #Calculo do inteiro
C = A-B
print("A parte Inteira é: %d"%B)
print("A parte fracionária é: %.f"%C) 