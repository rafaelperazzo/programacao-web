# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
c1 = int(input("Digite o numero da carta 1 :"))
c2 = int(input("Digite o numero da carta 2 :"))
c3 = int(input("Digite o numero da carta 3 :"))
c4 = int(input("Digite o numero da carta 4 :"))
c5 = int(input("Digite o numero da carta 5 :"))
c6 = int(input("Digite o numero da carta 6 :"))
if c1 > c2 and c1 > c3 and c1 > c4 and c1 > c5 and c1 > c6:
    if c2 > c3 and c3 > c4 and c4 > c5 and c5 > c6:
        print("D")
if c6 > c5 and c6 > c4 and c6 > c3 and c6 > c2 and c6 > c1:
    if c5 > c4 and c4 > c3 and c3 > c2 and c2 > c1:
        print("C")
else:
    print("N")
    


