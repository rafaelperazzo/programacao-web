# -*- coding: utf-8 -*-
print("_______________________\nCálculo de v\n_______________________")
p=float(input("n\nDigite o valor de P: "))
i=float(input("Digite o valor de i: "))
n=float(input("Digite o valor de n: "))
v=(p*(((1+i)**n)-1))/i
print("_______________________\n\nO resultado de v é: %.2f"%v)