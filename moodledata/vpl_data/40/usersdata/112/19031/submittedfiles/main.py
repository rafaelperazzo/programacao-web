# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
def fatorial(n):
   if n<=1:
      return 1
   else:
      return n*fatorial(n-1) 
n= float(raw_input('Digite o número:'))
fatorial(n)
print  fatorial(n)
    
    