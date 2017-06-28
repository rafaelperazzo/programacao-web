# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

def soma1(a,b):
    soma=0
    a=[]
    for i in range(0,len(a),1):
        soma=soma+(a[i]*b[i])
        c.insert(0,soma)
    return (c)
    return (soma)
def soma2(a):
    soma=0
    c=[]
    for i in range(0,len(a),1):
        soma=soma+a[i]
        c.insert(0,soma)
    return (c)
    return (soma)
def soma3(a):
    soma=0
    c=[]
    for i in range(0,len(a),1):
        soma=soma+(a[i]**2)
        c.insert(0,soma)
    return (c)
    return (soma)
n=int(input(' digite a quantidade de elementos da lista:'))

for i in range(0,n,1):
    x=[]
    m=float(input('digite um valor:'))
    x.insert(0,m)
for i in range(0,n,1):
    y=[]
    m=float(input('digite um valor:'))
    y.insert(0,m)

r=(n*(soma1(x,y))-(soma2(x)*soma2(y)))/((n*(soma3(x))-(soma2(x))**2)**0.5)*((n*(soma3(y))-(soma2(y))**2)**0.5)

print('soma de x=' %soma2(x))







