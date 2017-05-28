# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
anterior=0
anterior_menor=11
maior=1
for i in range(1,4,1):
    N=int(input("digite o número de alunos"))
    if N>anterior:
        maior=N
    else:
        maior=anterior
    anterior=maior
    if N < anterior_menor:
        menor=N
    else:
        menor=anterior_menor
    anterior_menor=menor
print(maior)
print(menor)