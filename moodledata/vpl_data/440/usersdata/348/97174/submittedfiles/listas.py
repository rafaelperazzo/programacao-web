# -*- coding: utf-8 -*-

n = int(input('informe quantidade de termos: '))
while n <= 2:
    n = int(input('informe quantidade de termos: '))

l1 = []

for i in range (0,n,1):
    l1.append(int(input('informe o %d° elemento da lista: ' %(i+1))))
   
resultado = 0
for i in range (1, len(l1)):
    atual = abs(l1[i-1]-l1[i])
    if atual > resultado:
        resultado = atual
        
print(resultado)