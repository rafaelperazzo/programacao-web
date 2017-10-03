# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
c1 = int(input("Digite o numero da carta 1 :"))
c2 = int(input("Digite o numero da carta 2 :"))
c3 = int(input("Digite o numero da carta 3 :"))
c4 = int(input("Digite o numero da carta 4 :"))
c5 = int(input("Digite o numero da carta 5 :"))
c6 = int(input("Digite o numero da carta 6 :"))
if 1<=c1<=13 and 1<=c2<=13 and 1<=c3<=13 and 1<=c4<=13 and 1<=c5<=13 and 1<=c6<=13:
    if c1 != c2 != c3 != c4 != c5 != c6:
        if c1 > c2 and c1 > c3 and c1 > c4 and c1 > c5 and c1 > c6:
            print("D")
elif c1 < c2 and c1 < c3 and c1 < c4 and c1 < c5 and c1 < c6:
    print("C")
elif c2 > c1 and c3 > c2 and c4 > c3 and c5 > c4 and c6 > c5:
    print("C")
