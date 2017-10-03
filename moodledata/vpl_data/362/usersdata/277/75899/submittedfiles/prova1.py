# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
c1 = int(input("digite carta [1-13]: "))
c2 = int(input("digite carta [1-13]: "))
c3 = int(input("digite carta [1-13]: "))
c4 = int(input("digite carta [1-13]: "))
c5 = int(input("digite carta [1-13]: "))

if (c1 < c2) and (c2 < c3) and (c3 < c4) and (c4 < c5) :
    print('C')
elif (c1 > c2) and (c2 > c3) and (c3 > c4) and (c4 > c5) :
    print('D')
else:
    print('N')
