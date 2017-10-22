# -*- coding: utf-8 -*-
n = int(input("digite um numero com 8 algarismos:  "))
t = 10000000
soma = 0
if n < 10000000 and n > 9999999:
    for i in range (0,8,1):
        soma = soma + (n//t)
        n = n%t
        t = t/10
    print ('%.d' % soma)
else:
    print("NAO SEI")



