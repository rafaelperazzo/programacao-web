# -*- coding: utf-8 -*-

investimento=float(input("Digite um valor: "))
taxa=float(input("Digite uma taxa: "))
while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))
saldo=(taxa*investimento)
while(True):
    investimento = investimento + saldo
    print(investimento)
    if investimento==investimento+(11*saldo):
        break