# -*- coding: utf-8 -*-
import math
a= int(input('Digite o Primeiro número:'))
b= int(input('Digite o Segundo número:'))

#MAIOR SEMPRE SERÁ "a"
if a<b:
    x=a
    a=b
    b=x

i=1

while i<=b:
    if b%i==0:
        MDC=i
        if a%MDC==0:
    print (MDC)
    i=i+1







