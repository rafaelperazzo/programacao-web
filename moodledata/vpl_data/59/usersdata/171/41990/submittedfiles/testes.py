# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite a base:'))
cont=0
produto=1
while cont<n-1:
    produto=produto*(n-1)
    n=n-1
print(produto)