# -*- coding: utf-8 -*-
m=int(input("Digite um número com oito algarismos:"))
while m<100000000 and m>9999999:
    m=(m%10000000)+(m%1000000)+(m%100000)+(m%10000)+(m%1000)+(m%100)+(m%10)+(m%1)
    print(m)
 
