# -*- coding: utf-8 -*-
import math
n=int(input('Digite a Quantidade de Múltiplos:'))
a=int(input('Digite o N1:'))
b=int(input('Digite o N2:'))
cont=0
i=1
while (cont<n):
    if (i%a==0) or (i%b==0):
        cont=cont+1
        print(i)
 i=i+1