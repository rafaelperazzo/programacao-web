# -*- coding: utf-8 -*-
c=int(input("Digite c: "))

ped=[]
unico=[]
estoque=[]

for i in range (0,c,1):
    ped.append(int(input("Digite um valor: ")))

for i in range (0,len(ped),1):
    for j in range (0,len(ped),1):
        if ped[i]!=ped[j]:
            unico.append(ped[i])
        else:
            del ped[i]

print(unico)

for i in range (0,c,1):
    estoque.append(0)
    

    
    