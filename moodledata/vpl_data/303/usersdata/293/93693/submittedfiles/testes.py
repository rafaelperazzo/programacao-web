# -*- coding: utf-8 -*-
elementos=[]
n=int(input("Digite o número de elementos: "))

for i in range(0,n,1):
    elementos.append(float(input("Digite o valor do %dº elemento: " %(i+1))))
media=sum(elementos)/len(elementos)
print("A média dos %d elementos é %.2f"%(n,media))
    