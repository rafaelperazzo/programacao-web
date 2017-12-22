# -*- coding: utf-8 -*-

resultado=0
n=int(input('Digite n : '))
for i in range (0,n,1):
    resultado= resultado + ((-1)**i)/(2*i+1)
print (resultado)