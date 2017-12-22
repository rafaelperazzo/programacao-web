# -*- coding: utf-8 -*-

n= int(input('Digite um número inteiro: '))
print(len(n))
def soma(n):
    for i in range(0,n+1,1):
        
        a= n//10
        b= n%10
        soma= a+b
    return soma





print(soma(n))
