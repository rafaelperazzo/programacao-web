# -*- coding: utf-8 -*-
m=int(input("Digite um número com oito algarismos:"))
while m<100000000 and m>9999999:
    m=(m%10000000)
    m=(m%1000000)
    print(m)
 
