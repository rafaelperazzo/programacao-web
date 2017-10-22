# -*- coding: utf-8 -*-

investimento=float(input("Digite um valor: "))
taxa=float(input("Digite uma taxa: "))
while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))
saldo=(taxa*investimento)
while(True):
    if investimento==investimento*((1+taxa)**10):
        investimento = investimento + saldo
        print(investimento)