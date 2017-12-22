# -*- coding: utf-8 -*-
c = int(input('insira o número de consultas:'))

l = []
for i in range (0,c,1):
  tam = int(input('Digite os tamanhos:')) 
  l.append(tam)

i = 0
while i < (len(l)+1):
  j = i + 1
  while j < len(l):
    if l[i] == l[j]:
      l.pop(j)
    else:
      j = j+1
      
  i = i+1
  
print ((len(l))*2)
