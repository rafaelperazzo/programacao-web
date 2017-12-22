# -*- coding: utf-8 -*-


n=int(input('digite a quantidade de numeros da lista: '))

a=[]
for i in range(1,n+1,1):
    numero=int(input('digite o numero de vidas para a sala: '))
    a.append(numero)
    
entrada=int(input('digite a porta de entrada: '))
saida=int(input('digite a porta de saida: '))
soma=0
i=entrada

while i<=saida:
    soma=soma+(a[i])
    i=i+1
    
print(soma)