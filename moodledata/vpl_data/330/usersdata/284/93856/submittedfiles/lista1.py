# -*- coding: utf-8 -*n
n=int(input('digite um numero: '))
numeros=[]
soma1=0
soma2=0
a=0
b=0
for i in range(0,n,1):
    numeros.append(int(input('digite o numero%.d: ' %(i+1))))
for i in range (0,n,1):
    if numeros[i]%2!=0:
        soma1=soma1+numeros[i]
        a=a+1
print(soma1)
for i in range(0,n,1):
    if numeros[i]%2==0:
        soma2=soma2+numeros[i]
        b=b+1
print(soma2)
print(a)
print(b)
print(numeros)


    
    

