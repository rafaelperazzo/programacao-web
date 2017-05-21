# -*- coding: utf-8 -*-
import math
n=int(input('Informe o número de termos: '))
a=int(input('Informe o 1° Termo: '))
b=int(input('Informe o 2° Termo: '))

multiplo=1
contador=0
while contador<=n :
    if (multiplo%a==0) or (multiplo%b==0):
        print(multiplo)
    multiplo=multiplo+1
    contador=contador+1