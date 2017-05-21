# -*- coding: utf-8 -*-
import math
n = int(input('Digite o numero de divisores: '))
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
cont=0
multiplo=1
while cont<n:
    if (multiplo%a==0) or (multiplo%b==0):
        cont = cont+1
        print(multiplo)
    multiplo=multiplo+1    
