# -*- coding: utf-8 -*-
n = int(input("digite um numero com 8 algarismos:  "))
soma = 0
t = 10000000
if n < 1000000 and n > 9999999:
    for i in range (0,8,1):
        soma = soma + (n//t)
        n = n%t
        t = t/10
    print ('%.d' % soma)
else:
    print("NAO SEI")



