# -*- coding: utf-8 -*-
#ENTRADA
D1 = int(input("Dia 1: "))
M1 = int(input("Mes 1: "))
A1 = int(input("Ano 1: "))
D2 = int(input("Dia 2: "))
M2 = int(input("Mes 2: "))
A2 = int(input("Ano 2: "))
#Processamento
if (D1>D2) and (M1>M1) and (A1>A2):
    print("Data 01")
if (D1<D2) and (M1<M2) and (A1<A2):
    print("Data 02")
if (D1==D2) and (M1==M2) and (A1==A2):
    print ("Iguais")
