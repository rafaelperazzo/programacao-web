# -*- coding: utf-8 -*-
"""
TEMPO ESTIMADO: 20 min
"""
n = int(input('Digite n: '))
numeros=[]
for i in range(n):
  while(True):
    num = int(input('Digite num inteiro: '))
    if num not in numeros:
      numeros.append(num)
      break
pares=[]
impares=[]
for i in range(n):
  if (numeros[i]%2==0):
    pares.append(numeros[i])
  else:
    impares.append(numeros[i])
print(numeros)
print(pares)
print(impares)