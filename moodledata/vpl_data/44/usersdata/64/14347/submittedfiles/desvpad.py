# -*- coding: utf-8 -*-
from __future__ import division

n = input("Digite a quantidade de valores: ")
a = []
i = 1
media = 0

while i<=n:
    a.append(input("Digite o valor da lista: "))
    media = sum(a)/n
    
    i = i + 1
    
print("%.2f" %a[0])
print ("%.2f" %a[n-1])
print ("%.2f" %(media))
print (a)

z= 0
soma = 0

for i in range (1, n+1, 1):
    soma = ((a[z]-media)**2)+soma
    z = z+1
    
soma =(soma)*(1/(n-1))
soma = soma**(1/2)
print("%.2f" %(soma))