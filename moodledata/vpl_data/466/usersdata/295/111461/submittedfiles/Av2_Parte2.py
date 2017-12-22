# -*- coding: utf-8 -*-
a=[]
b=[]
c=[]
n=int(input("Digite o numero de elementos da lista:"))
for i in range(0,n):
    a.append(int(input("digite os elementos da lista a :")))
i=1
contcres=0
contdecres=0
contc=0
if contcres:
    contcres=contcres+1
    print ("S")


if contdecres:
    contdecres=contdecres-1
    print("N")
else:
    print("N")

if contc:
    contc=contc+0
    print("S")
else:
    print("N")

