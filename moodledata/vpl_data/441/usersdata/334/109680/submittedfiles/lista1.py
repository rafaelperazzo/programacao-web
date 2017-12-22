# -*- coding: utf-8 -*-

n = int(input())

l = []
for i in range(n):
    l.append(int(input()))

soma_impar = 0
soma_par = 0
q_impar = 0
q_par = 0
for i in range(n):
    if l[i]%2==0:
        soma_par += l[i]
        q_par += 1
    else:
        soma_impar += l[i]
        q_impar += 1

print(soma_impar)
print(soma_par)
print(q_impar)
print(q_par)