# -*- coding: utf-8 -*-
#COMECE AQUI
while True:
    a=int(input('Digite a:'))
    if a>0:
        break
soma=0
while a>=1:
    i=a//10
    r=a%10
    soma=soma+r
    a=a//10
print (soma)