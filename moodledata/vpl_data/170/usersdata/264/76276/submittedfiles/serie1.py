# -*- coding: utf-8 -*-
import math
termos= int(input('digite a quantidade de termos:'))
soma=0
i=1
while (i<=termos):
    if (i%2)==0:
        soma= soma - (i/(i*i))
    else:
        soma= soma + (i/(i*i))
    i= i + 1
print ('%.5f' %soma)