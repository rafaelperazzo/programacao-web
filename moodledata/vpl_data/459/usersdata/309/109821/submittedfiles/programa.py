# -*- coding: utf-8 -*-

n=int(input("Digite quantidade de consultas:"))
lista=[]
somat=0
for i in range(n):
  a=int(input("Digite o tamanho do taco:"))
  if len(lista)>=1:
    if a in lista:
      somat=somat+2
      lista.remove(a)
    else:
      lista.append(a)
  else:
    lista.append(a)

tamanho=len(lista)*2+somat
print (tamanho)

