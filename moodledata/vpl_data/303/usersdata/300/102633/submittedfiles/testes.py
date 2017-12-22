# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

soma = 0
for i in range(0,len(lista),1):
    soma = soma + lista[i]
media = soma/len(lista)  
cont = 0
for i in range(0,len(lista),1):
    p = lista[i] - media
    h = p**2
    cont = cont + h
variancia = cont/len(lista)    
print('%.2f' % variancia)
    