# -*- coding: utf-8 -*-
n = int(input("Digite um valor: "))
a = []
for i in range(0,n,1):
    x = int(input("digite um valor: "))
    a.append(x)
print("%.2f" % a[0])
print("%.2f" % a[len(a)-1])
soma=0
for e in range (0,len(a),1):
    soma=a[e]+soma
media=soma/lem(a)
print
print

