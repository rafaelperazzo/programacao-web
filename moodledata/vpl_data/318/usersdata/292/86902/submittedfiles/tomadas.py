# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
def tomadas(T1, T2, T3, T4):
    max_not = T1 + T2 + T3 + T4 - 3
    return max_not

T1 = int(input("Digite o número de tomadas da régua 1: "))
while T1<=1:
    T1 = int(input("Dados inválidos! Digite novamente: "))
T2 = int(input("Digite o número de tomadas da régua 2: "))
while T2<=1:
    T2 = int(input("Dados inválidos! Digite novamente: "))
T3 = int(input("Digite o número de tomadas da régua 3: "))
while T3<=1:
    T3 = int(input("Dados inválidos! Digite novamente: "))
T4 = int(input("Digite o número de tomadas da régua 4: "))
while T4<=1:
    T4 = int(input("Dados inválidos! Digite novamente: "))
print(tomadas(T1, T2, T3, T4))