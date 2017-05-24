# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
a=int(input('Digite o valor de A: '))
b=int(input('Digite o valor de B: '))
c=int(input('Digite o valor de C: '))
d=int(input('Digite o valor de D: '))
if (a<b<c<d) and a>0 and b>0 and c>0 and d>0 and a<=13 and b<=13 and c<=13 and d<=13:
    print('C')
elif (a>b>c>d)and a>0 and b>0 and c>0 and d>0 and a<=13 and b<=13 and c<=13 and d<=13:
    print('D')
else:
    print('N')



