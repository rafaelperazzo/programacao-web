# -*- coding: utf-8 -*-


while True:
    m = int(input( 'informe linhas: '))
    if m >= 2 and m <= 1000:
        break
while True:
    n = int(input( 'informe colunas: '))
    if n >= 2 and n <= 1000:
        break

matriz =[]
for i in range (m):
    linhas = []
    for j in range (n):
        linhas.append(int(input('informe os elementos: ')))
    matriz.append(linhas)

k = 10000
for h in range (m):
    s = 0
   for g in range (n):
        s = s + matriz[g][h]
    if k > s:
    k = s 
print(k)
    
   



    