# -*- coding: utf-8 -*-
n = int(input('Digite o valor de n: '))
a = []
soma = 0

for i in range (0,n,1):
    a.append(int(input('Digite um valor: ')))
    if (a[i])%2==0:
        soma = soma + a[i]
        
print(soma)

for i in range (0,n,1):
    a.append(int(input('Digite um valor: ')))
    if (a[i])%2!=0:
        soma = soma + a[i]
        
print(soma) 

for i in range (0,n,1):
    a.append(int(input('Digite um valor: ')))
    if (a[i])%2==0:
        soma = soma + 1
        
print(soma)

for i in range (0,n,1):
    a.append(int(input('Digite um valor: ')))
    if (a[i])%2!=0:
        soma = soma + 1
        
print(soma)

print(a)


  
        
        

    
    

