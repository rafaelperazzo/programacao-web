# -*- coding: utf-8 -*-

i=1000

while i<=9999:
    G=i//100
    P=i%100
    soma=G+P
    raiz= i**(1/2)
    if raiz==soma:
        print(i)
    i=i+1
    

