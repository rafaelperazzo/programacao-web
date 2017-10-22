# -*- coding: utf-8 -*-
mat=int(input("---------------------------------\nDigite a matricula do aluno: "))

nota1=float(input("\n---------------------------------\nDigite a primeira nota do aluno: "))
nota2=float(input("\n---------------------------------\nDigite a segunda nota do aluno: "))
nota3=float(input("\n---------------------------------\nDigite a terceira nota do aluno: "))
me=float(input("\n---------------------------------\nDigite a dos exercícios do aluno: "))

ma=((nota1)+(nota2*2)+(nota3*3)+(me))/7

if ma>=9:
    print(A)
elif ma<9 and ma>=7.5:
    print(B)
elif ma<7.5 and ma>=6:
    print(C)
elif ma<6 and ma>=4:
    print(D)
elif ma<4:
    print(E)

