# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
sm = float(input("DIGITE SEU SALDO MÉDIO: "))
if 0<=sm<=500:
    print("%.2f" % sm)
    if 0<=sm<=500:
        print("NENHUM CRÉDITO")
if 501<=sm<=1000:
    print(sm)
    if 501<=sm<=1000:
        print((sm*30)/100)