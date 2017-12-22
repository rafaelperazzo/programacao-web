# -*- coding: utf-8 -*-

def resposta(a,b):
    n=0
    m=0
    while True:
        if a[n]==b[m]:
            cont=cont+1
        if m<=len(b):
            m=m+1
        if m>len(b):
            m==0
            n=n+1
        if n>len(a):
            break
    return(cont)
    
    
    
A=int(input('Digite o tamanho da list de a : '))
B=int(input('Digite o tamanho da list de b : '))

a=[]
b=[]

for i in range(0,a,1):
    valora=int(input('Digite o termo de a : '))
    a.append(valora)
for i in range(0,b,1):
    valorb=int(input('Digite o termo de a : '))
    a.append(valorb)

print(resposta(a,b))



