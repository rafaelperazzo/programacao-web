# -*- coding: utf-8 -*-
a=int(input('digite o valor de a: '))
b=int(input('digite o valor de b: '))
def digitos(numero):
    cont=0
    while (numero>0):
        cont=cont+1
        numero=numero//10
    return(cont)
cont=digitos(b)
x9=0
while (a>0):
    if a%(10**cont)==b:
        x9=x9+1
    a=a//10
if x9==0:
    print('N')
else :
    print('S')