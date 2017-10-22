# -*- coding: utf-8 -*-
m=int(input("Digite um número com dois algarismos:"))
while m<100 and m>9:
    m=(m+0)+(m+10)+(m+100)+(m+1000)+(m+10000)+(m+100000)+(m+1000000)
    print(m)
 
