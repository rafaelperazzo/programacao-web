# -*- coding: utf-8 -*-
n = int(input('alunos :'))
p = int(input('pontos :'))
cont = 0

for i in range(0,n,1) :
    nota1 = float(input('primeira nota :'))
    nota2 = float(input('segunda nota : '))
    pontos = nota1 + nota2
    if (pontos>=p) :
        cont = cont + 1
    pontos = 0
print(cont)