# -*- coding: utf-8 -*-
import math
a=int(input('Digite a:'))
b=int(input('Digite b:'))

numerador=a
denominador=b
while (numerador%denominador)>=0:
    resto=numerador%denominador
    if resto>0:
        mdc=resto
    numerador=denominador
    denominador=resto
print(mdc)    
    