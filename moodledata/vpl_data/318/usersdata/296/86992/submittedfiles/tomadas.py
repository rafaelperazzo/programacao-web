# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
T1 = int(input("Digite o número de tomadas da primeira régua: "))
while T1 <=1:
    T1 = int(input("Digite o número de tomadas da primeira régua: "))
T2 = int(input("Digite o número de tomadas da segunda régua: "))
while T2 <=1:
    T2 = int(input("Digite o número de tomadas da segunda régua: "))
T3 = int(input("Digite o número de tomadas da terceira régua: "))
while T3<=1:
    T3 = int(input("Digite o número de tomadas da terceira régua: "))
T4 = int(input("Digite o número de tomadas da quarta régua: "))
while T4 <=1:
    T4 = int(input("Digite o número de tomadas da quarta régua: "))
cont = 1
while cont <= 4:
    tomadas = T4*cont
    cont = cont+1
print(T4)
    
    
    
    
    
