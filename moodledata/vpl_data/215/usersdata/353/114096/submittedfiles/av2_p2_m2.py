# -*- coding: utf-8 -*-

n=int(input('salas'))

a=[n]
for i in range(1,n+1,1):
    a.append(input('vida'))
    


entrada=int(input('entrada'))
saida=int(input('saida'))

soma=0
while entrada<=saida :
    soma=soma+ (a[entrada])
    entrada=entrada+1
    
print (soma)


for i in range (entrada,saida):
    soma = soma + a[i]
print(soma)
    
    
