# -*- coding: utf-8 -*-

investimento=float(input("Digite um valor: "))
taxa=float(input("Digite uma taxa: "))
while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))
while investimento<3000 :
    print(investimento)
    investimento= investimento+taxa*investimento
