# -*- coding: utf-8 -*-

notas=[]
for i in range(1,51,1):
    notas.append(float(input("Digite a %dº nota: " %i)))
media=sum(notas)/len(notas)
print(media)
