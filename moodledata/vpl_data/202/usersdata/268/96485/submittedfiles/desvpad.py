# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('Digite o numero de termos : '))
a=[]
soma=0

for i in range(0,n,1):
    valor=int(input('Digite o termo :'))
    a.append(valor)
    soma=soma+valor
media=soma/len(a)

somatorio=0
for i in range (0,len(a),1):
    somatorio= somatorio + (a[i] - media)**2
    
delta=(1/n-1)**somatorio
var=(delta)**(1/2)

print(a[0])
print(a[n-1])
print(media)
print(var)
    
