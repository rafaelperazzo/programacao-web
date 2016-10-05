# -*- coding: utf-8 -*-
from __future__ import division
import math
 # ENTRADA
n = int(input("Digite n:"))
a = int(input("Digite a:"))
b = int(input("Digite b:"))
    
#PROCESSAMENTO    
# mult é o candidato a multiplo de a ou b
i= 1
contador= 0
while (contador < n):
        if (i%a ==0) or i%b == 0:
            contador = contador+1
            print(i)
            
        i = i + 1	
