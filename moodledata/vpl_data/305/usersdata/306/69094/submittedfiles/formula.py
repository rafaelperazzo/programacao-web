# -*- coding: utf-8 -*-
print("Cálculo de v")
p=float(input("\n\n\nDigite o valor de P: "))
i=float(input("\nDigite o valor de i: "))
n=float(input("\nDigite o valor de n: "))
v=(p*(((1+i)**n)-1))/i
print("_______________________\n\nO resultado de v é:%.2f"%v)