# -*- coding: utf-8 -*-
#função verificandoLecker
def verificandoLecker(lista, quantidade):
  verificador=0
  for k in range(1,quantidade-1,1):
    if lista[k-1]<lista[k] and lista[k]>lista[k+1]:
      verificador=1+verificador
     
  if verificador==1:
    print("S")
  else:
    print("N")
    
    
    
#Cód. Principal
qtelementos=int(input("Digite a quantidade de elementos das suas listas:"))
lista1=[]
lista2=[]
for i in range (0,qtelementos,1):
  lista1.append(float(input("Digite um elemento para sua lista 1:")))

for j in range (0,qtelementos,1):
    lista2.append(float(input("Digite um elemento para sua lista 2:")))
verificandoLecker(lista1, qtelementos)
verificandoLecker(lista2, qtelementos)


