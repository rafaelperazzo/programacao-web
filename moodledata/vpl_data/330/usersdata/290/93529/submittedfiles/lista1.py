# -*- coding: utf-8 -*-
n=int(input("Digite o valor de n: "))
lista=[]
for i in range(o,n,1):
    lista.append(float(input("Digite o valor para a lista: ")))
a=0
b=0
c=0
d=0
for i in range(0,n,1):
    if lista[i]%2!=0:
        a=a+i
        c=c+1
    else:
        b=b+i
        d=d+1
print(a)
print(b)
print(c)
print(d)
print(lista)


    
    

