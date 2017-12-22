# -*- coding: utf-8 -*-
n=int(input('Digite o número de postos: '))
m=int(input('Digite a distância in termediária máxima: '))
a=[]

for i in range (0,n,1):
    a.append(int(input('Didite a posição dos postos de água: ')))

resultado=0
for j in range (0,len(a),1):
    if j==0:
        resultado=resultado+0
    else:
        resultado=resultado+(a[j]-a[j-1])

if (resultado>=42195):
    print('S')
else:
    print('N')

