#coding: utf-8
n=int(input('digite n: '))
soma=0
termo=1
denominador=2
while termo<=n:
    soma=soma+1/denominador
    termo=termo+1
    denominador=denominador+2
    print(soma)