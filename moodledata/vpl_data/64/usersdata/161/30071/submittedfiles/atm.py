# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CODIGO AQUI
valor=int(input('Informe o valor em dinheiro: '))

if (valor%20)==0:
    print(valor//20)
    print('%d'%0)
    print('%d'%0)
    print('%d'%0)
    print('%d'%0)
    
if (valor%20)!=0 and (valor%10==0):
    print(valor//20)
    print((valor-((valor//20)*20))//10)
    print('%d'%0)
    print('%d'%0)
    print('%d'%0)
    
if (valor%20)!=0 and (valor%10)!=0 and (valor%5)==0:
    print(valor//20)
    print((valor-((valor//20)*20))//10)
    print((valor-((valor//10)*10))//5)
    print('%d'%0)
    print('%d'%0)

    
if (valor%20)!=0 and (valor%10)!=0 and (valor%5)!=0 and (valor%2)==0:
    print(valor//20)
    print((valor-((valor//20)*20))//10)
    print((valor-((valor//10)*10))//5)
    print((valor-((valor//5)*5))/2)
    print('%d'%0)
    
if (valor%20)!=0 and (valor%10)!=0 and (valor%5)!=0 and (valor%2)!=0:
    print(valor//20)
    print((valor-((valor//20)*20))//10)
    print((valor-((valor//10)*10))//5)
    print((valor-((valor//5)*5))//2)
    print(valor-((valor//2)*2))
