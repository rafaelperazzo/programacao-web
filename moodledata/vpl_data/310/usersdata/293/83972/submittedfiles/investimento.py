# -*- coding: utf-8 -*-

investimento=float(input("Digite um valor: "))
taxa=float(input("Digite uma taxa: "))
valor=0
while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))
saldo=(taxa*investimento)
while(true):
    investimento= investimento + saldo
    if investimento==investimento*((1+taxa)**10):
        break
print(investimento)