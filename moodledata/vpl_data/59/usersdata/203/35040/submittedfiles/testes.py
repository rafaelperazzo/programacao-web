#coding: utf-8
n=int(input('digite n: '))
x=int(input('digite x: '))
y=1
soma=0
denominador=1
for i in range(1,n+1,1):
    soma=soma+y*((x**denominador)/denominador)
    denominador=denominador+2
    y=y*(-1)
print(soma)