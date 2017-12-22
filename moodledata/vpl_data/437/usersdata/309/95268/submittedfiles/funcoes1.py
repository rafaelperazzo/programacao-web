# -*- coding: utf-8 -*-

# Inicio da função p/ verificação de lista crescente 
def crescente (lista):
   k=0
   for i in range (0,n,1):
       
       if lista[i]<lista[i+1]:
           k=k+1
   if k==n:
        print("S")
   else:
        print("N")
        
# Fim da função crescente 


def decrescente (lista):
   k=0
   for i in range (0,n,1):
       
       if lista[i]>lista[i+1]:
           k=k+1
   if k==n:
        print("S")
   else:
        print("N")
        



def vl_consecutivos (lista):
   k=0
   for i in range (0,n,1):
       
       if lista[i]==lista[i+1]:
           k=k+1
   if k!=0:
        print("S")
   else:
        print("N")
        
        
        
#Programa principal

n=int(input("Olá, seja bem vindo ao easy, digite um n:"))

a = []
for i in range (0,n,1):
    a.append(int(input("Digite o  elemento da lista A:")))

b = []
for i in range (0,n,1):
    b.append(int(input("Digite o  elemento da lista B:")))

c = []
for i in range (0,n,1):
    c.append(int(input("Digite o  elemento da lista C:")))
    

# para a lista A
crescente(a[])
descrescente(a)
vl_consecutivos (a)







