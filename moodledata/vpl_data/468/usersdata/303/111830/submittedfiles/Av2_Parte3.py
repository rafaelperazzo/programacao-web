# -*- coding: utf-8 -*-
#n=int(input('Digite a quantidade de listas:'))
#for i in range(0,n,1):
    #m=int(input('Digite a quantidade de termos da lista:'))
    #for j in range(0,m,1):
        #x=int(input('Digite um termo:'))
        #x.append(m)
while True:
    a=int(input('Digite a:'))
    if a>0:
        break

soma=0
while a>=1:
    i=a//10
    r=a%10
    soma=soma + r
    a=a//10
print(soma)
    
    
