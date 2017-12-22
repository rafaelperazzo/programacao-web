# -*- coding: utf-8 -*-
c=int(input("Digite c: "))

ped=[]
unico=[]
estoque=[]

for i in range (0,c,1):
    ped.append(int(input("Digite um valor: ")))

for i in ped:
    if i not in unico:
        unico.append(i)
    

print(unico)

for i in range (0,c,1):
    estoque.append(0)
    

    
    