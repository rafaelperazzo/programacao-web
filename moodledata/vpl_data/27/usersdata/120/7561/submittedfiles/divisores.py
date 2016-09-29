# -*- coding: utf-8 -*-
from __future__ import division
import math
 # ENTRADA
n = int(input("Digite n:"))
a = int(input("Digite a:"))
b = int(input("Digite b:"))
    
#PROCESSAMENTO    
# mult é o candidato a multiplo de a ou b
mult= 0
contador= 0
while contador < n:
        if mult%a == 0 or mult%b == 0:
            print(mult)
            contador = contador+1;
        mult = mult + 1;	
