# -*- coding: utf-8 -*-
import math
n=int(input('digite a quantidade de divisores:'))
a=int(input('digite um valor para a:'))
b=int(input('digite um valor para b:'))
contador=0
multiplo=1
while contador<n:
    if (multiplo%a)==0 or (multiplo%b)==0:
        contador=contador+1
        print(multiplo)
    multiplo=multiplo+1    
        