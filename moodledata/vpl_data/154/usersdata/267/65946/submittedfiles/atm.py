# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
valor = int(input('Insira o valor à sacar: '))
#PROCESSAMENTO
c20 = valor//20
valor2 = valor%20
c10 = valor2//10
valor3 = valor2%10
c5 = valor3//5
valor4 = valor3%5

print(c20)
print(c10)
print(c5)

print(valor2)
print(valor3)
print(valor4)