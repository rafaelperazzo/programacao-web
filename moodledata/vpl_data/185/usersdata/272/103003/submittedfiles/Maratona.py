# -*- coding: utf-8 -*-
n=int(input('Digite o número de postos: '))
m=int(input('Digite a distância in termediária máxima: '))
a=[]

for i in range (0,n,1):
    a.append(int(input('Didite a posição dos postos de água: ')))

cont=0
for j in range (0,len(a),1):
    if j==0:
        0==0
    else:
        if (a[j]-a[j-1])<=m:
            cont=cont+1
            

if (cont==len(a)-1):
    print('S')
else:
    print('N')

