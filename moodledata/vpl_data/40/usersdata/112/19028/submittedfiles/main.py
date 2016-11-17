# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
n=input('Digite o número:')
def fatorial(n):
   if n<=1:
      return 1
   else:
      return n*fatorial(n-1) 
n= float(raw_input("Insira um numero natural n \n"))
fatorial(n)
print "O fatorial de n eh: \n", fatorial(n)
    
    