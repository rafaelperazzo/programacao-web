# -*- coding: utf-8 -*-
print("###################################################################")
print("Seja muito bem vindo! Venha comigo calcular infinitas diagonais! ;D)
print("###################################################################")
cont=0
while cont!=1:
    n=int(input("\nDigite o número de lados do polígono convexo: ")
    if n>=3:
        Nd=(n*(n-3))/2
        print("\nEste polígono tem %.1f diagonais"%Nd)
        cont=int(input("\n\nDeseja continuar? (1 para encerrar e outro número para continuar): "))
    else:
        print("\nNão existe um polígono com %d lados!!!"%n)
        import os
        os.system("pause")
        