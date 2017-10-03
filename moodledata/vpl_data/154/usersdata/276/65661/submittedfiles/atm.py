# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
valor = int(input('Digite o valor: '))

nota20 = valor//20
resto20 = valor - (nota20*20)

nota10 = resto20//10
resto10 = resto20 - (nota10*10)

nota5 = resto10//5
resto5 = resto10 - (nota5*5)

nota2 = resto5//2
resto2 = resto5 - (nota2*2)

nota1 = resto2//1

print (nota20)
print (nota10)
print (nota5)
print (nota2)
print (nota1)
