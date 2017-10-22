# -*- coding: utf-8 -*-
import math
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
mdc=1
if n1>n2:
    for i in range (2,n2,1):
        if n1%i!=0 and n2%i!=0:
            mdc*=i
        return mdc
    
    
