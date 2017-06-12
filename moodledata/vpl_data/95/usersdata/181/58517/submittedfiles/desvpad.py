# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
a=[]
soma1=0
soma2=0
for i in range (0,n,1):
    soma1=soma1+a[i]
media=soma1/len(a)
    
for i in range (0,n,1):
    soma2=soma2+((a[i]-media)**2)
    DesvPad=(soma2/n+1)**0.5    

for i in range (1,n+1,1):
    numero=float(input('digite numero:'))
    a.append(numero)

print(a[0])
print(a[i])
print(media)
print('%.2f'%DesvPad)