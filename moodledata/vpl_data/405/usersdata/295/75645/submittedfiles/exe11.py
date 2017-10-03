# -*- coding: utf-8 -*-
a = int(input("Digite um numero :"))
soma = 0 
i = 1 
while 1 <= a:
    soma = soma + i
    i = i + 1
if 10000000<=a<=99999999:
    print("soma dos ", a , " algarismos", soma)
else:
    print("NAO SEI")

