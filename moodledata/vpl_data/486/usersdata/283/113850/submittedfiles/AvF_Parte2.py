# -*- coding: utf-8 -*-
n=int(input('Digite o número de alunos: '))
a=[]
for i in range(0,n,1):
    b=[]
    for j in range(0,1,1):
        x = int(input('Digite a idade do aluno: '))
        if x == -1:
            break
        while x<18:
            print('Idade inválida')
            x = int(input('Digite a idade do aluno: '))
        y = float(input('Digite a altura do aluno: '))
        while y < 0 : 
            print('Altura inválida')
            y = float(input('Digite a altura do aluno: '))
        b.append(x)
        b.append(y)
    a.append(b)
c=[]
for l in range(0,n,1):
    c.append(a[l][1])
d = sum(c)/n
print(d)
cont=0
for k in range(0,n,1):
    if a[k][0] >= 25 and a[k][1] < d:
        cont += 1
print(cont)        



