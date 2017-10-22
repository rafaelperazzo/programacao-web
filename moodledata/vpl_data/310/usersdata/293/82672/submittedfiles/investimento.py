# -*- coding: utf-8 -*-

investimento=float(input("Digite um valor: "))
taxa=float(input("Digite uma taxa: "))

while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))
saldo=investimento+taxa*investimento

while (True):
    if saldo>=investimento*((1+taxa)**10):
        break
    saldo=saldo+saldo
    print(saldo)
