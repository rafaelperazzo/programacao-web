# -*- coding: utf-8 -*-
import random
#COMECE AQUI ABAIXO
while True:
    n = int(input('Digite quantidade de alunos: '))
    if n>0:
        break
notas =[]
media = 0
for i in range(0,n,1):
    notas.append(random.randint(0,10))

for i in range (0,n,1):
    media+= notas[i]/float(n)
    print (notas[i])
print (media)

