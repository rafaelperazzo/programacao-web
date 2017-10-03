# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
sm = float(input("Digite seu saldo médio: "))
if 0<=sm<=500:
    print ("Seu saldo médio é "+str("%.2f" % sm))
    if 0<=sm<=500:
        print("Nenhum crédito")
if 501<=sm<=1000:
    print("Seu saldo médio é "+str("%.2f" % sm))
    if 501<=sm<=1000:
        print("Seu crédito é "+str("%.2f" % ((sm*30)/100)))
if 1001<=sm<=3000:
    print("Seu saldo médio é "+str("%.2f" % sm))
    if 1001<=sm<=3000:
        print("Seu crédito é "+str("%.2f" % ((sm*40)/100)))
if sm>3000:
    print("Seu saldo médio é "+str("%.2f" % sm))
    if sm>3000:
         print("Seu crédito é "+str("%.2f" % ((sm*50)/100)))