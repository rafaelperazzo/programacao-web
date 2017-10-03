# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
a=int(input("Carta1: "))
b=int(input("Carta2: "))
c=int(input("Carta3: "))
d=int(input("Carta4: "))
e=int(input("Carta5: "))
f=int(input("Carta6: "))
if a<b and b<c and c<d and d<e and e<f:
    print("C")
elif f<e and e<d and d<c and c<b and b<a:
    print("D")
else:
    print("N")
aa=1
bb=2
cc=1
dd=not(aa==bb or bb!=cc) and c
print(dd)