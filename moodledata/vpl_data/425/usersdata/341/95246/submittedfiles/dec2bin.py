# -*- coding: utf-8 -*-

x = int(input('Digite x: '))
y = int(input('Digite y: '))
def digitos(numero):
    cont=0
    while (numero>0):
        cont=cont+1
        numero=numero//10
    return(cont)
cont=digitos(x)
w9=0
while (y>0):
    if (y%(10**cont))==x:
        w9 = w9 + 1
    y=y//10
if w9==0:
    print('N')
else:
    print('S')



