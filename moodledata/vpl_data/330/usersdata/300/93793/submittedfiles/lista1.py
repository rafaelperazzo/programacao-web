# -*- coding: utf-8 -*-
n = int(input('Digite o valor de n: '))
a = []
soma1 = 0
soma2 = 0
quant1 = 0
quant2 = 0

for i in range (0,n,1):
    a.append(int(input('Digite um valor: ')))
    if (a[i])%2==0:
        soma1 = soma1 + a[i]
        
for i in range (0,n,1):
    a.append(int(input('Digite um valor: ')))
    if (a[i])%2 == 1:
        soma2 = soma2 + a[i]

for i in range (0,n,1):
    a.append(int(input('Digite um valor: ')))
    if (a[i])%2==0:
        quant1 = quant1 + 1

for i in range (0,n,1):
    a.append(int(input('Digite um valor: ')))
    if (a[i])%2!=0:
        quant2 = quant2 + 1
        
print(soma1)
print(soma2) 
print(quant1)
print(quant2)

print(a)


  
        
        

    
    

