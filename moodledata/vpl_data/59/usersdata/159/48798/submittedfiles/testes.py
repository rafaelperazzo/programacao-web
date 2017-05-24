# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('Digite a:'))
b=int(input('Digite b:'))
if a<=b:
    n=a
else:
    n=b
for i in range (1,n+1,1):
    if a%i==0:
        if b%i==0:
            mdc=i
print(mdc)            