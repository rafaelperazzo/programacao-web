# -*- coding: utf-8 -*-
import math
n = int(input('Digite o numero de multiplos desejados: '))
a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
multiplo=0
i=0
while i<n:
    if multiplo%a==0 or multiplo%b==0:
        print (multiplo)
        k+=1
    multiplo+=1
    