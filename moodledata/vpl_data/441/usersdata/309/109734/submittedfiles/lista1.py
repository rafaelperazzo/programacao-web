# -*- coding: utf-8 -*-

n=int(input("Digite um n:"))
lista=[]

for i in range (n):
  lista.append(int(input("Digite um elmento para sua lista:")))

contpar=0
somatPar=0
contimpar=0
somatImpar=0
for j in range (n):
  if lista[j]%2==0:
    contpar+=1
    somatPar+=lista[j]
  else:
    contimpar+=1
    somatImpar+=lista[j]
    
print(somatImpar)
print(somatPar)
print(contimpar)
print(contpar)
print(lista)
    

