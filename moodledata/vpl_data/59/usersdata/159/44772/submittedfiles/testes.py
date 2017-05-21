# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
a=0
for i in range (1,n+1,1):
    x=int(input('Digite a nota:'))
    if x>=a:
        a=x
    else:
        b=x
print(a)
print(b)