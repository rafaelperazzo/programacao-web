# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
Maior_nota_anterior=0
Menor_nota_anterior=0
b=0
n=int(input("digite o número de alunos"))
Maior_nota_anterior=0
Menor_nota_anterior=0
for i in range(1,n+1,1):
    a=float(input("digite a nota"))
    if Maior_nota_anterior>a:
        maior=Maior_nota_anterior
        if Menor_nota_anterior<a:
            menor=Menor_nota_anterior
        else:
            menor=a
        Menor_nota_anterior=menor
        Maior_nota_anterior=maior
    else:
        maior=a
        if Menor_nota_anterior<a:
            menor=Menor_nota_anterior
        else:
            menor=a
        Menor_nota_anterior=menor
        Maior_nota_anterior=maior
print(maior)
print(menor)