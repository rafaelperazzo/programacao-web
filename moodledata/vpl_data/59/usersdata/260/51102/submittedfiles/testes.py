# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
anterior=0
for i in range(1,4,1):
    q=int(input("digite o número de alunos"))
    if q>anterior:
        maior=q
        dia=i
    else:
        maior=anterior
    print(maior)
    print(dia)