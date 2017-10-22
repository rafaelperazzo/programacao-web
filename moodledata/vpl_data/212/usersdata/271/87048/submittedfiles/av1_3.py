# -*- coding: utf-8 -*-
import math
#ENTRADA
a = int(input('Digite o valor de a : '))
b = int(input('Digite o valor de b : '))
c = int(input('Digite o valor de c : '))
#PROCESSAMENTO
mmc = 2
while (mmc>0) :
    if (a%mmc==0) and (b%mmc==0) and (c%mmc==0) :
        print(mmc)
        break
    mmc = mmc+1


            
        
