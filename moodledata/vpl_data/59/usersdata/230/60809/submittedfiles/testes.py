# -*- coding: utf-8 -*-
import math
def algarismo(n):
    a=[]
    while(n!=0) :
        a.append(n%10)
        n=n//10
    return(a)
    
def soma2(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+(a[i])**2
    return(soma)
    
    
n=int(input('Digite valor: '))
while n//10!=0:
    b=algarismo(n)
    n=soma2(b)
if n==1:
    print('Feliz')
if n!=1:
    print('Não Feliz')