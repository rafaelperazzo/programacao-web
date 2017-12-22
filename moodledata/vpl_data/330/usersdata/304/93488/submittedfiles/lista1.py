# -*- coding: utf-8 -*-

n = int(input('Digite n: '))
a = []
for i in range (0,n,1):
    a.append(int(input('Digite um valor: ')))
somapar = 0
somaimpar = 0
for i in range (0,n,1):
    if a[i] % 2 == 0:
        somapar = somapar + 1
    else:
        somaimpar = somaimpar + 1
print(somaimpar)
print(somapar)
print(a[i])