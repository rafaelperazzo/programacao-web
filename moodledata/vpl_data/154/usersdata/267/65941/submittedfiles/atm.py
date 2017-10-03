# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
valor = int(input('insira o valor à sacar: '))
#PROCESSAMENTO
c20 = valor//20
valor2 = valor%20
c10 = (valor2)//10
valor3 = valor2%10

print(c20)
print(c10)
print(valor2)
print(valor3)