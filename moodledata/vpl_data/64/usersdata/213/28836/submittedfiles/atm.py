# -*- coding: utf-8 -*-
from __future__ import division
import math

valor=int(input('Informe o valor a ser sacado:'))

restodivisao20=valor%20
restodivisao10=restodivisao20%10
restodivisao5=restodivisao10%5
restodivisao2=restodivisao5%2
restodivisao1=restodivisao2

if restodivisao20==0 :
    print(valor/20)
    print(0)
    print(0)
    print(0)
    print(0)
    
elif restodivisao20!=0 and restodivisao10==0:
    print(valor//20)
    resto=(valor//20)*20
    print((valor-resto)/10)
    print(0)
    print(0)
    print(0)

elif restodivisao20!=0 and restodivisao10!=0 and restodivisao5==0:
    print(valor//20)
    resto=(valor//20)*20
    print((valor-resto)//10)
    resto=(valor//10)*10
    print((valor-resto)/5)
    print(0)
    print(0)

elif restodivisao20!=0 and restodivisao10!=0 and restodivisao5!=0 and restodivisao2==0:
    print(valor//20)
    resto=(valor//20)*20
    print((valor-resto)//10)
    resto=(valor//10)*10
    print((valor-resto)//5)
    resto=(valor//5)*5
    print((valor-resto)/2)
    print(0)

else:
    print(valor//20)
    resto=(valor//20)*20
    print((valor-resto)//10)
    resto=(valor//10)*10
    print((valor-resto)//5)
    resto=(valor//5)*5
    print((valor-resto)/2)
    print(valor%2)

