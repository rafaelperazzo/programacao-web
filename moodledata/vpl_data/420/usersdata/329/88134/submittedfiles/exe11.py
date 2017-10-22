# -*- coding: utf-8 -*-
n = int(input("digite um numero com 8 algarismos:"))
soma = 0
while n < 100000000 and n > 9999999 :
    for i in range (0,8,1):
        resto = n % 10
        n = (n - resto)/10
        soma = soma + resto
    print ('%d' % soma)
    break
else:
    print("NAO SEI")
   
                
    




