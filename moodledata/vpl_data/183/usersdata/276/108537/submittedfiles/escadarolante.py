# -*- coding: utf-8 -*-

N=int(input('Digite a quantidade de pessoas'))

soma=0
a=[]
for i in range (0,N,1):
    T=int(input('Digite o tempo que cada pessoa passou pelo sensor'))
    a.append(T)
    
tempo = 0

for j in range (0,N,1):
    if j==0:
        resultado = resultado
    else:
        resultado = resultado + (a[j]-a[j-1])
resposta= tempo + 10

print(resposta)