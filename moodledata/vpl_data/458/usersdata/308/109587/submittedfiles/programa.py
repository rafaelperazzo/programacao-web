# -*- coding: utf-8 -*-
n = int(input(''))
while n<3:
    n = int(input(''))

usuario = []

for i in range(n):
    usuario.append([])
    for j in range(n):
        usuario[i].append(int(input('')))

todos = []
for i in range(n):
    for j in range(n):
        x = sum(usuario[i])- usuario[i][j]
        for k in range(n):
            x+= usuario[k][j]
        x -= usuario[i][j]
        todos.append(x)
        
print(max(todos))

