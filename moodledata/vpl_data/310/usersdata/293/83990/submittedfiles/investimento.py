# -*- coding: utf-8 -*-

investimento=float(input("Digite um valor: "))
taxa=float(input("Digite uma taxa: "))
while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))

while(True):
    investimento = investimento + taxa*investimento
    print(investimento)
    if investimento==investimento+(11*taxa*investimento):
        break