# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

a=int(input('digite a:'))
b=int(input('digite b:'))
n=int(input('digite a quantidade múltiplos:'))

cont=0
i=1
while cont<n:
    cont=cont+i*a and cont=cont+i*b
    i=i+1
print(cont)
