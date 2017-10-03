# -*- coding: utf-8 -*-
#ENTRADA
D1 = int(input("Dia 1: "))
M1 = int(input("Mes 1: "))
A1 = int(input("Ano 1: "))
D2 = int(input("Dia 2: "))
M2 = int(input("Mes 2: "))
A2 = int(input("Ano 2: "))
#Processamento
if (A1>A2):
    print ("DATA1")
if (A1<A2):
    print ("DATA2")
if (A1==A2) and (M1>M2):
    print ("DATA1")
if (A1==A2) and (M1<M2):
    print ("DATA2")
if (A1==A2) and (M1==M2) and (D1>D2):
    print ("DATA1")
if (A1==A2) and (M1==M2) and (D1<D2):
    print ("DATA2")
if (D1==D2) and (M1==M2) and (A1==A2):
    print ("Iguais")
