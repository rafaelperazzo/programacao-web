# -*- coding: utf-8 -*-
from __future__ import division

n = input("Digite a quantidade de valores: ")

a = []

i = 0

media = 0

while i<=n:
    
    a.append(input("Digite o valor da lista: "))
    
    
    
    media = ((media + a[i])/n)
    
    
    i = i + 1
    
print(a[0])

print (media)