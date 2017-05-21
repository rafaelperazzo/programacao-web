# -*- coding: utf-8 -*-
import math
n=int(input('Digite quantidade de múltiplos: '))
a=int(input('Digite número 1: '))
b=int(input('Digite número 2: '))
cont=0
i=1
while cont<n:
     if i%a==0 or i%b==0:
         cont=cont+1
         print(i)
     i=i+1   
