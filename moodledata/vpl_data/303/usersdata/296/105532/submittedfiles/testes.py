# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#ENTRADA
#n = int(input("Digite o valor de n: "))
#a = []
#for i in range(0,n,1):
#    a.append(int(input('Digite um valor: ')))
#media = sum(a)/len(a)
#soma = 0
#for i in range(0,n,1):
#    soma += (a[i] - media)**2
#    desvio = ((1/(n-1)*soma))**0.5 
#print(desvio)
matriz = []
m = int(input("Digite o número de quadras no sentido norte-sul: "))
while m<=2 or m>=1000:
    m = int(input("Digite o número de quadras no sentido norte-sul: "))
n = int(input("Digite o número de quadras no sentido leste-oeste: "))
while n<=2 or n>=1000:
    n = int(input("Digite o número de quadras no sentido leste-oeste: "))
for i in range (0,m,1):
    linha = []
    for j in range (0,n,1):
        while True:
            x = int(input("Digite o valor da respectiva quadra: "))
            if (x>=1 or x<=100):
                break
        linha.append(x)
    matriz.append(linha)
menor = ((100*m)+1)
for j in range (0,n,1):
    soma = 0
    for i in range (0,m,1):
        soma += matriz[i][j]
    if soma < menor:
        menor = soma
print (menor)