# -*- coding: utf-8 -*-
import math
n = int(input("Digite n: "))
i = int(input("Digite i: "))
j = int(input("Digite j: "))
 
cont = 0 #conta quantos múltiplos foram impressos.
cm = 0 #candidato a múltiplo.
while cont < n:
    if cm%i == 0 or cm%j == 0:
        print(cm)
        cont += 1
    cm += 1