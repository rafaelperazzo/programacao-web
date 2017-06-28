# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

def soma(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    return soma
def somaproduto(a,b):
    soma=0
    c=[]
    for i in range(0,len(a),1):
        soma=soma+(a[i]*b[i])
        c.append(soma)
    return(soma)
def somaquadrado(a):
    soma=0
    c=[]
    for i in range(0,len(a),1):
        soma=soma+a[i]**2
        c.append(soma)
    return(soma)

n=int(input('digite o numero de elementos da lista:'))

for i in range(0,n,1):
    x=[]
    m=float(input('digite um elemento da lista x:'))
    x.append(m)
for i in range(0,n,1):
    y=[]
    m=float(input('digite um elemento da lista y:'))
    y.append(m)
a=somaproduto(x,y)
b=soma(x)
c=soma(y)
d=somaquadrado(x)
e=somaquadrado(y)

r=((n*a)-(b*c))/(((n*d)-b**2)**0.5)*(((n*e)-c**2)**0.5)

print(r)





