# -*- coding: utf-8 -*-
while True:
    m = int(input('quadras no sentido leste-oeste: '))
    if m>=2 and m<=1000:
        break
    
while True:
    n = int(input('quadras no sentido norte-sul: '))
    if n>=2 and n<=1000:
        break
bairro = []
for i in range(0,n,1):
    v = []
    for j in range(0,m,1):
        v.append(int(input('valores das quadras: ')))
    bairro.append(v)
mt = []
for i in range(n):
    v = []
    for j in range(m):
        v.append(bairro[j][i])
    mt.append(v)

som = 1000
for i in range(n):
    if sum(mt[i])<som:
        som=sum(mt[i])
print(som)