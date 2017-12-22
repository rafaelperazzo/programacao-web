# -*- coding: utf-8 -*-

notas=[]
n=int(input("Digite a quantidade de notas: "))
for i in range(1,n+1,1):
    notas.append(float(input("Digite a %dº nota: " %i)))
media=sum(notas)/len(notas)
print(media)
