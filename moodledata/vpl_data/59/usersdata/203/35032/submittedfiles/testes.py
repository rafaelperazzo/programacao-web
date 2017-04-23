#coding: utf-8
x=int(input('digite x: '))
soma=0
termo=1
for i in range(1,n+1,1):
    soma=soma+(x**termo/termo)
    termo=termo+2
    print(soma)