# -*- coding: utf-8 -*-

investimento=float(input("Digite um valor: "))
taxa=float(input("Digite uma taxa: "))
while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))
juros=1+taxa
while investimento<investimento*juros**10 :
    print("%.2f" %(investimento))
    investimento= investimento+taxa*investimento