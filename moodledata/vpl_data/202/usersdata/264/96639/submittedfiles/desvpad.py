# -*- coding: utf-8 -*-
import math

#comece abaixo
n= int(input('Digite o valor dos n elementos:'))
a= []
soma=0

for i in range(0,n,1):
    valor= int(input('Digite o valor de cada um dos termos da lista:'))
    a.append (valor)
    soma= soma+valor
media= soma/len(a)

somatorio=0
for i in range (0,len(a),1):
    somatorio= somatorio+ (a[i]-media)**2
delta= (1/(n-1))*somatorio
var= (delta)**(1/2)

print ('%.2f' %a[0])
print ('%.2f' %a[len(a)-1])
print ('%.2f' %media)
print ('%.2f' %var)