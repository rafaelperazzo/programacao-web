# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor = int(input('Digite o valor que deseja sacar: '))

notas20 = int(valor//20)
resto20 = int(valor%20)

notas10 = int(resto20//10)
resto10 = int(resto20%10)

notas5 = int(resto10//5)
resto5 = int(resto10%5)

notas2 = int(resto5//2)
resto2 = int(resto5%2)

notas1 = int(resto2//1)

print(notas20)
print(notas10)
print(notas5)
print(notas2)
print(notas1)