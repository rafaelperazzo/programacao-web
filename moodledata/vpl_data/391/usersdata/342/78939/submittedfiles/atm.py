# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
x = int(input('Valor a ser sacado:'))
nota20 = (x//20)
resto20 = (x-(nota20*20))
nota10 = (resto20//10)
resto10 = (x-((nota20*20)+(nota10)))
nota5 = (resto10//5)
resto5 = (x-((nota20*20)+(nota10*10)+(nota5*5)))
nota2 = (resto5//2)
resto2 = (x-((nota20*20)+(nota10*10)+(nota5*5)+(nota2*2)))
nota1 = (resto2//1)

print (nota20)
print (nota10)
print (nota5)
print (nota2)
print (nota1)
