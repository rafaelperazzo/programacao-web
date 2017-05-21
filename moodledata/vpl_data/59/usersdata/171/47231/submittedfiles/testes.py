# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
produto=1
for i in range(1,n+1,1):
    produto=produto*n
    n=n-1
print(produto)