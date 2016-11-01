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

print (media)