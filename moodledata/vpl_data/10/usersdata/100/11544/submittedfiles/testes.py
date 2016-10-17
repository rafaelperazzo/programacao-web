# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
s=0
c=1
x=1
# B será o valor binário a ser convertido
b= input ('Digite o valor binário:')
#programa para ver quando digitos tem b
s=0
c=1
x=1
while x<b:
    b = b//10
    c=c+1
    x=x+1
print c

#fim do bloco, faz-se agora um programa que elevara os valos de  c
for i in range (0, c, 1):
    r = b%10
    d = r*(2**i)
    s =s+d
    b=b//10
    print r