# -*- coding: utf-8 -*-
import math
n=int(input('Digite n:'))
a=int(input('Digite a:'))
b=int(input('Digite b:'))
contador=0
multiplo=1
while contador<n:
    if multiplo%a==0 or multiplo%b==0:
        print(multiplo)
        contador=contador+1
    multiplo=multiplo+1
    