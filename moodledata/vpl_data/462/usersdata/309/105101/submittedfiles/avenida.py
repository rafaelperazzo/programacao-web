# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de quadras no sentido N-S:"))
while m<2 or m>1000:
    print("Valor fora do intervalo!")
    m=int(input("Digite a quantidade de quadras no sentido N-S:"))
    
n=int(input("Digite a quantidade de quadras no sentido O-L:"))
while n<2 or n>1000:
    print("Valor fora do intervalo!")
    n=int(input("Digite a quantidade de quadras no sentido O-L:"))

mat=[]

for i in range (m):
    lista=[]
    for j in range (n):
        lista.append(int(input("Digite o valor da quandra:")))
    mat.append(lista)
    
    



