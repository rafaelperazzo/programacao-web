# -*- coding: utf-8 -*-



    
n=int(input('Digite a quantidade de elementos da lista a:'))
a=[]
for i in range(1,n+1,1):
    valor1=int(input('Digite os elementos da lista de a:'))
    a.append(valor1)
    
m=int(input('Digite a quantidade de elementos da lista b:'))
b=[]
for i  in range(1,m+1,1):
    valor2=int(input('Digite os elementos da lista de b:'))
    b.append(valor2)

cont=0
for i in range(0,len(b),1):
    if b[i] in a:
        cont=cont+1
print(contido(b))
        