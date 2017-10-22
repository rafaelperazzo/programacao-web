# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
T1 = int(input("Digite um número de tomadas da régua 1: "))
while (T1<=1):
    print("o número digitado é menor ou igual a 1")
    print("Digite outro número")
    T1 = int(input("Digite um número de tomadas da régua 1: "))
T2 = int(input("Digite um número de tomadas da régua 2: "))
while (T2<=1):
    print("o número digitado é menor ou igual a 1")
    print("Digite outro número")
    T2 = int(input("Digite um número de tomadas da régua 2: "))    
T3 = int(input("Digite um número de tomadas da régua 3: "))
while (T3<=1):
    print("o número digitado é menor ou igual a 1")
    print("Digite outro número")
    T1 = int(input("Digite um número de tomadas da régua 3: "))
T4 = int(input("Digite um número de tomadas da régua 4: "))
while (T4<=1):
    print("o número digitado é menor ou igual a 1")
    print("Digite outro número")
    T1 = int(input("Digite um número de tomadas da régua 4: "))
total = (T1+T2+T3+T4)-3
print(total)