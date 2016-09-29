# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
#entrada
v = int( input('Digite o valor que deseja sacar: '))

#processamento:
notasde20 = v//20
notasde10 = (v%20)//10
notasde5 = ((v%20)%10)//5
notasde2 = (((v%20)%10)%5)//2
notasde1 = (((v%20)%10)%5)%2

#saída:
print (notasde20)