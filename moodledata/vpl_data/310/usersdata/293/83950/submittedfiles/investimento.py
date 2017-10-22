# -*- coding: utf-8 -*-

investimento=float(input("Digite um valor: "))
taxa=float(input("Digite uma taxa: "))
valor=0
while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))
saldo=taxa*investimento
for i in range (1,11,saldo):
    saldo=investimento + i
    print(saldo)