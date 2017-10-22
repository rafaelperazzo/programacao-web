# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

a=int(input('Digite a: '))
b=int(input('Digite b: '))

i=1
mdc=0

while (i<=a):
    if (a%i==0) and (b%i==0):
        mdc=i
    i=i+1
print(mdc)
    

