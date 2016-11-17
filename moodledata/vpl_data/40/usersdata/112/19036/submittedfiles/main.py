# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

def fatorial(n):
   if n<=1:
      return 1
   else:
      return n*fatorial(n-1) 
n= float(raw_input('Digite o número:'))
fatorial(n)
print  fatorial(n)


def cospos(numero):
    x=input ('Digite o valor de x')  
    soma=0
    for i in range (2,n,4):
        if partepositiva==(x**i)/fatorial(i):
            soma=soma+partepositiva
            return soma
        else:
            return None
        print(soma)
def cosneg(numero):
    soma=0
    for i in range (4,n,4):
        if partenegativa==(x**i)/fatorial(i):
            soma=soma+partenegativa
            return soma
        else:
            return None
        print(soma)