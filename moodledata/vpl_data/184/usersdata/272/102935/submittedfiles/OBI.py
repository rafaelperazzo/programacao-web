# -*- coding: utf-8 -*-
n=int(input('Digite o número de participantes: '))
p=int(input('Digite o número mínimo de pontos: '))
a=[]

for i in range (0,(2*n),1):
    a.append(int(input('Digite as notas de cada participante: '))

resultado=0
for j in range (0,len(a),1):
    if (j%2==0):
        if ((a[j]+a[j+1])>=p):
            resultado=resultado+1
print(resultado)