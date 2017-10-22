# -*- coding: utf-8 -*-
a=int(input('a: '))
b=int(input('b: '))

def digitos(numero):
    cont=0
    while (numero>0):
        cont=cont+1
        numero=numero//10
    return(cont)
cont=digitos(a)
c=0
while b>0:
    if b%(10**cont)==a:
        c=c+1
    b=b//10
if c==0:
    print(('N')
else:
    print('S')
