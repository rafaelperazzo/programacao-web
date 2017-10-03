# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
c1 = int(input("Digite o numero da carta 1 :"))
c2 = int(input("Digite o numero da carta 2 :"))
c3 = int(input("Digite o numero da carta 3 :"))
c4 = int(input("Digite o numero da carta 4 :"))
c5 = int(input("Digite o numero da carta 5 :"))
c6 = int(input("Digite o numero da carta 6 :"))
if c2 > c1 and c3 > c2 and c4 > c3 and c5 > c4 and c6 > c5:
            print("C")
if c2 < c1 and c3 < c2 and c4 < c3 and c5 < c4 and c6 < c5:
            print("D")
else:
    print("N")
    


