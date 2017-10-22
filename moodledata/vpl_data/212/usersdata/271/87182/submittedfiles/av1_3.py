# -*- coding: utf-8 -*-
import math
#ENTRADA
a = int(input('Digite o valor de a : '))
b = int(input('Digite o valor de b : '))
c = int(input('Digite o valor de c : '))
#PROCESSAMENTO
i = 2
while (i>0) :
    if (c>b) and (b>a) :
        if (c%b==0) and (c%a==0) :
            mmc = c
            print(mmc)
            break
    c = c * i

    

            
        
