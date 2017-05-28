# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
anterior=0
maior=1
for i in range(1,4,1):
    q=int(input("digite o número de alunos"))
    if maior>anterior:
        maior=q
        dia=i
    else:
        maior=anterior
    anterior=q
    print(maior)
    print(dia)