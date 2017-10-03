# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI

Valor=int(input(' Valor a ser sacado: '))

C20= Valor//20

resto20= Valor - C20*20

C10= resto20//10

resto10= resto20 - C10*10

C5= resto10//5

resto5= resto10 - C5*5

C2 = resto5//2

resto2= resto5 - C2*2

C1 = resto2//1

print(C20)
print(C10)
print(C5)
print(C2)
print(C1)