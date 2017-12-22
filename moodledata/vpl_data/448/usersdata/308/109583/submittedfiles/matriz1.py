# -*- coding: utf-8 -*-
n = int(input(''))
m = int(input(''))

usuario = []
for i in range(n):
    usuario.append([])
    for j in range(m):
        usuario[i].append(int(input('')))
invertida = []
for i in range(n):
    invertida.append([])
    for j in range(m):
        invertida[i].append(usuario[n-1-i][m-1-j])
print(invertida)
