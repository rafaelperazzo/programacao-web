# -*- coding: utf-8 -*-
a= int(input('Digite o valor de a:'))
b= int(input('Digite o valor de b:'))
def digitos(numero):
    cont= 0
    while (numero>0):
        cont= cont+1
        numero= numero//10
    return(cont)
cont= digitos(a)
x9= 0
while (b>0):
    if (b%(10**cont))==a:
        x9= x9+1
    b=b//10
if x9==0:
    print('N')
else:
    print('S')
