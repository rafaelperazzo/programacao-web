# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
lista = [1,2,3,4,5]
soma = 0
for i in range(0,len(lista),1):
    soma = soma + lista[i]
media = soma/len(lista)
print (media)
cont = 0
for i in range(0,len(lista),1):
    p = lista[i] - media
    h = p**2
    cont = cont + h
variancia = cont/len(lista)    
print('%.2f' % variancia)
    