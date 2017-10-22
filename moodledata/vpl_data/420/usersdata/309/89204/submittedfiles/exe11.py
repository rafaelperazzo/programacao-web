# -*- coding: utf-8 -*-

num= int(input("Digite um algarismo com 8 digitos:"))

K=100000000
b=0
x=0

while (x<8):
    num=num//K
    
    if (num==0):
        print ("NAO SEI")
    
    K=K/10
    b=b+num
    x=x+1
    