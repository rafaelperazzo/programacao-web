# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número: '))
b=int(input('Digite um número: '))
ndedivisoes=0
if b>a:
    mdc=a
    maior=b
    menor=a
elif a>b:
    mdc=b
    maior=a
    menor=b
cont=0
while resto>0:
    resto=maior%menor
    divisao=menor%resto
    menor=maior//menor
    maior=menor
    cont=cont+1
    mdc=resto
print(mdc)
print(cont)    
    



#while a%mdc!=0 or b%mdc!=0:
#   mdc=mdc-1
#    ndedivisoes=ndedivisoes+1
#print(mdc)    
#print(ndedivisoes)
