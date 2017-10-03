# -*- coding: utf-8 -*-
n = int(input('Digite o valor de n: '))
i = 1
somatorio = 0
while (i<n):
    if (n%i==0):
        print (i)
        somatorio = somatorio + i 
    i = i + 1

if (somatorio == n):
    print ('PERFEITO')
else:
    print ('NÃO PEFEITO')