# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('n:'))
a=int(input('a:'))
b=int(input('b:'))
mult=1
cont=0
while cont<n:
    if mult%a==0 or mult%b==0:
        print(mult)
        cont=cont+1
    mult=mult+1