# -*- coding: utf-8 -*-
import os
n = int(input("Digite o número de itens da lista: "))
print("\n")
os.system("clear")
k = []

for i in range(1,n+1):
    k.append(int(input("Digite o %d valor: "%i)))

