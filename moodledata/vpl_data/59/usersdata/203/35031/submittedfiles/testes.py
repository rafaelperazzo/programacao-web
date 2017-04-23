#coding: utf-8
n=int(input('digite n: '))
soma=0
denominador=2
for i in range (1,n+1,1):
    soma=soma+1/denominador
    denominador=denominador+2
    print(soma)