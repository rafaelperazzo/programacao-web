#coding: utf-8
n=int(input('digite n: '))
soma=0
for i in range (2,n+1,2):
    soma=soma+(1/i)
    print(soma)