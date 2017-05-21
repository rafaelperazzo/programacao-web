# -*- coding: utf-8 -*-
import math
n=int(input('Informe o número de termos: '))
a=int(input('Informe o 1° Termo: '))
b=int(input('Informe o 2° Termo: '))

multiplo=1
contador=1
while contador<=n:
    if (a%multiplo==0) or (b%multiplo==0):
        multiplo=multiplo+1
        contador=contador+1
        print(multiplo)