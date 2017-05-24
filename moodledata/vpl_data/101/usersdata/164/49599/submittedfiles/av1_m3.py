# -*- coding: utf-8 -*-
import math
m=int(input('Digite o número de termos: '))
cont=0
soma=3
a=0
b=2
for i in range (1, m+1, 1):
    a=4/(b*(b+1)*(b+2))
    cont=cont+1
    if (cont%2==1):
        soma=soma+a
    if (cont%2==0):
        soma=soma-a
    b=b+2    
print('%.6f' %soma)        
