# -*- coding: utf-8 -*-
import math
#COMECE SEU CODIGO AQUI
soma=0
for i in range(1,5,1):
    tn=int(input(' Digite t{} : '.format(i)))
    while(tn<1):
        tn=int(input(' Digite t{} : '.format(i)))
    soma=soma+tn      
print(soma)    