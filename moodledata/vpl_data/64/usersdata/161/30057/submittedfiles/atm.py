# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CODIGO AQUI
valor=int(input('Informe o valor em dinheiro: '))

if (valor%20)==0:
    print(valor/20)
    print('0')
    print('0')
    print('0')
    print('0')
if (valor%20)!=0: and (valor%10==0):
    print(valor//20)
    print((valor-(valor//20))//10)
    print('0')
    print('0')
    print('0')
if (valor%20)!=0: and (valor%10)!=0 and (valor%5)==0:
    print(valor//20)
    print((valor-(valor//20))//10)
    print((valor-(valor//20)-(valor//10))//5)
    print('0')
if (valor%20)!=0: and (valor%10)!=0 and (valor%5)!=0 and (valor%2)==0:
    print(valor//20)
    print((valor-(valor//20))//10)
    print((valor-(valor//20)-(valor//10))//5)
    print((valor-(valor//20)-(valor//10)-(valo//5))/2)
    print('0')
if (valor%20)!=0: and (valor%10)!=0 and (valor%5)!=0 and (valor%2)!=0:
    print(valor//20)
    print((valor-(valor//20))/10)
    print((valor-(valor//20)-(valor//10))//5)
    print((valor-(valor//20)-(valor//10)-(valor//5))//2)
    print((valor-(valor//20)-(valor//10)-(valor//5)-(valor//2))
 