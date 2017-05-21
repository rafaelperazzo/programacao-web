# -*- coding: utf-8 -*-
import math
n=int(input('Informe o número de termos: '))
a=int(input('Informe o 1° Termo: '))
b=int(input('Informe o 2° Termo: '))

multiplo=1

for i in range (1,n+1,1):
    if (a%multiplo==0) or (b%multiplo==0):
        multipli=multiplo+1
        print(multiplo)