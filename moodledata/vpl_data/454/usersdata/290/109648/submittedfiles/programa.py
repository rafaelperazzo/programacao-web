# -*- coding: utf-8 -*-
c=int(input("Digite o número de consultas ao estoque: "))
estoque=[]
f=0
for i in range(0,c,1):
    d=int(input(""Digite o comprimento do taco: "))
    if d not in estoque:
        f=f+2
    estoque.append(d)
print(f)