# -*- coding: utf-8 -*-
def menor(a, b):
    if a==b:
        menor=a
    if a<b:
        menor=a
    if a>b:
        menor=b
    return menor

n=int(input('Digite o numero de seçoes da piscina: '))
alturas=[]
for i in range (0, n, 1):
    alturas.append(int(input('Digite a altura da seçao %d: ' % (i+1))))

crescente=[]
for i in range (0, n-1, 1):
    if alturas[i]<alturas[i+1]:
        crescente.append('S')
    else:
        crescente.append('N')
if alturas[n-1]>alturas[n-2]:
        crescente.append('S')
if not alturas[n-1]>alturas[n-2]:
        crescente.append('N')

decrescente=[]
for i in range (0, n-1, 1):
    if alturas[i]>alturas[i+1]:
        crescente.append('S')
    else:
        crescente.append('N')
if alturas[n-1]<alturas[n-2]:
        crescente.append('S')
if not alturas[n-1]<alturas[n-2]:
        crescente.append('N')

picos=[]
for i in range (0, len(cresecente), 1):
    if crescente[i]==decrescente[i]:
        picos.append[i]

cont=0
k=menor(alturas[0], alturas[picos[0]])
for i in range (1, alturas[picos[0]], 1):
    if alturas[i]<k:
        cont+=1

for i in range (0, len(picos)-1, 1):
    j=menor(picos[i], picos[i+1])
    for h in range (alturas[picos[i]]+1, alturas[picos[i+1]], 1):
        if alturas[h]<j:
            cont+=1

g=menor(alturas[picos[len(picos)-1]], alturas[n-1])
for i in range (picos[len(picos)-1]+1, n, 1):
    if alturas[i]<g:
        cont+=1

print(cont)