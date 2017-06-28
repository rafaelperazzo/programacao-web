# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

def soma1(a,b):
    soma=0
    c=[]
    for i in range(0,len(a),1):
        soma=soma+(a[i]*b[i])
        c.insert(0,soma)
    return soma and (c)
def soma2(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    return soma
def soma3(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+(a[i]**2)
    return soma
    
n=int(input(' digite a quantidade de elementos da lista:'))
x=[]
y=[]
for i in range(0,n,1):
    m=float(input('digite um valor para a lista x:'))
    x.insert(0,m)
for i in range(0,n,1):
    m=float(input('digite um valor para a lista y:'))
    y.insert(0,m)

print(soma2(x))
print(soma2(y))
print(soma3(x))
print(soma3(y))
print(soma1(x,y))






