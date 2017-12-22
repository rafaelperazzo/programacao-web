# -*- coding: utf-8 -*-
m=[]
n=int(input("Digite a ordem da matriz:"))
for i in range (n):
    lista=[]
    for j in range (n):
      lista.append(int(input('Digite um elemento:')))
    m.append(lista)
  
h=0      
for i in range(n):
    o=sum(m[i])-(m[i][i])
    if m[i][i]>o:
        h=h+1
        
if h<n:
    print("NAO")
else:
    print("SIM")
