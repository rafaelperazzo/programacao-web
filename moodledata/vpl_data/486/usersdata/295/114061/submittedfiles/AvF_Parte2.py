# -*- coding: utf-8 -*-
n = 01

m = int(input("Digite sua idade: "))
for i in range(1,n+100):    
    while m<18:
        m = int(input("Digite sua idade: "))
        if m =='-1':
            break

n = int(input("Digite sua altura: "))
for i in range(1,n+100):
    while n<0:
        n = int(input("Digite sua altura: "))
    
