# -*- coding: utf-8 -*-
P = float(input("Digite o valor do peso: "))
h = float(input("Digite o valor da altura: "))
IMC = (P/(h)**2)
if IMC<20:
    print("ABAIXO")
elif 20<=IMC<=25:
    print("NORMAL")
    


