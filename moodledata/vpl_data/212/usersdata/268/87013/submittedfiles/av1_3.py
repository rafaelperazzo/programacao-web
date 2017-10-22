# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor do primeiro numero: '))
b=int(input('Digite o valor do segundo numero: '))
c=int(input('Digite o valor do terceiro numero: '))
i=1
 while True:
     if i%a==0 and i%b==0 and i%c==0:
         MMC=i
         break
     else:
         i=i+1
print(MMC)