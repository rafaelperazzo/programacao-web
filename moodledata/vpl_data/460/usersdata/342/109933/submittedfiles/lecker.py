# -*- coding: utf-8 -*-
def lecker(lista):
  soma = 0
  if lista[0] > lista[1]:
    soma = soma + 1
  if lista[len(lista)-1] > lista[len(lista)-2]:
    soma = soma + 1
  for i in range (n-2):
    if lista[1] < lista[i-1] and lista[i+1] > lista[i+2]:
      soma = soma + 1
  if soma == 1:
    print ('S')
  else:
    print('N')
    
    
n = int(input('insrira a quantidade dos elementos: '))
lista1 = []
lista2 = []

for i in range(0,n,1):
  lista1.append(int(input('insira o elementos da primeira lista:')))
for i in range(0,n,1):
  lista2.append(int(input('insira o elementos da segunda lista:')))
  
lecker(lista1)
lecker(lista2)

  


  
  
      
    
  
  
  
  

  



    


