# -*- coding: utf-8 -*-

def resposta(a,b):
    x=0
    y=0
    cont=0
    while True:
        if a[x]==b[y]:
             cont=cont+1
        if y<=len(b):
             y=y+1
        if y>len(b):
             y=0
             x=x+1
        if x>len(a):
             break
    return(cont)
    
    
    
m=int(input('Digite o tamanho da list de a : '))
n=int(input('Digite o tamanho da list de b : '))

a=[]
b=[]

for i in range(0,m,1):
    valora=int(input('Digite o termo de a : '))
    a.append(valora)
for i in range(0,n,1):
    valorb=int(input('Digite o termo de b : '))
    b.append(valorb)

print(resposta(a,b))



