# -*- coding: utf-8 -*-
n=int(input('Digite o número de alunos: '))
a=[]
for i in range(0,n,1):
    b=[]
    for j in range(0,1,1):
        x = int(input('Digite a idade do aluno: '))
        y = float(input('Digite a altura do aluno: '))
        if x == -1:
            break
        while y < 0 : 
            print('Altura inválida')
            y = float(input('Digite a altura do aluno: '))
            
        b.append(x)
        b.append(y)
    a.append(b)
print(a)