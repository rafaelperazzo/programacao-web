# -*- coding: utf-8 -*-
#####DESVIO PADRÃO########
elementos=[]
soma_1=0
n=int(input("Digite o número de elementos: "))
while(True):
    if n<=0:
        n=int(input("Digite o número de elementos: "))
    else:
        break
    
for i in range(0,n,1):
    elementos.append(float(input("Digite o valor do %dº elemento: " %(i+1))))
media=sum(elementos)/len(elementos)

for i in range(0,n,1):
    soma_1=((elementos[i]-media)**2)+ soma_1
desv=((1/n)*soma_1)**0.5

print("A média dos %d elementos é %.2f"%(n,media))

print("O desvio padrão dos %d elementos é %.3f"%(n,desv))
    