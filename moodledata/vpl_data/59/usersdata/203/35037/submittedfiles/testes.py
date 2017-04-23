#coding: utf-8
n=int(input('digite n: '))
x=int(input('digite x: '))
y=1
soma=0
termo=1
for i in range(1,n+1,1):
    soma=soma+y*((x**termo)/termo)
    termo=termo+2
    y=y*(-1)
    print(soma)