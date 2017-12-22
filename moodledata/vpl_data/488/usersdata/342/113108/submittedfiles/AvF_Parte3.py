# -*- coding: utf-8 -*-
n = int(input('digite a quantidade de elementos:'))
l = []
lpar = []
limpar = []

for i in range (n):
    val = int(input('insira um número'))
    l.append(val)
    if val%2 == 0:
        lpar.append(val)
    else:
        limpar.append(val)
        
print (l)
print (lpar)
print (limpar)