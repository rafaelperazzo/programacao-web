# -*- coding: utf-8 -*-
n=int(input("Digite o número de pessoas: "))
i=0
termo=0
while termo>0:
    idade=int(input("Digite a idade das pessoas: "))
    i=i+idade
    termo=termo-1
media=(i/n)
print("%.2f"%media)
