#coding: utf-8
n=int(input('digite n: '))
x=int(input('digite x: '))
soma=0
denominador=1
for i in range(1,n+1,1):
    if i%2==0:
        soma=soma-((x**denominador)/denominador)
    else:
        soma=soma+((x**denominador)/denominador)
    denominador=denominador+2
print(soma)