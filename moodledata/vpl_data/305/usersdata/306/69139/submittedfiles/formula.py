# -*- coding: utf-8 -*-
print("-----------------------\nCálculo de v\n-----------------------")
p=float(input("\nDigite o valor de P: "))
i=float(input("Digite o valor de i: "))
n=float(input("Digite o valor de n: "))
v=(p*(((1+i)**n)-1))/i
print("_______________________\n\nO resultado de v é: %.2f"%v)