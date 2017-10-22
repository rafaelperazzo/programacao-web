# -*- coding: utf-8 -*-

investimento=float(input("Digite um valor: "))
valor=0
taxa=float(input("Digite uma taxa: "))

while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))
saldo=investimento+taxa*investimento
while (True):
    if valor==10000:
        break
    valor=saldo+valor
    print(valor)
