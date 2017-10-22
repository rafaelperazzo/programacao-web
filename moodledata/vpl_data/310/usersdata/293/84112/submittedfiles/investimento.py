# -*- coding: utf-8 -*-

investimento=float(input("Digite um valor: "))
taxa=float(input("Digite uma taxa: "))
while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))
while investimento<=investimento+(10*(taxa*investimento)):
    print("%.2f" %(investimento))
    investimento= investimento+taxa*investimento