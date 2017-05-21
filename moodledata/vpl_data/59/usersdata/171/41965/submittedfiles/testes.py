# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
a=int(input('digite a base:'))
b=int(input('digite o expoente:'))
cont=0
produto=1
while cont<b:
    produto=produto*a
    cont=cont+1
print(produto)
