#coding: utf-8
n=int(input('digite n: '))
x=1
soma=0
termo=1
for i in range(1,n+1,1):
    soma=soma+((x**termo)/termo)
    termo=termo+2
    print(soma)