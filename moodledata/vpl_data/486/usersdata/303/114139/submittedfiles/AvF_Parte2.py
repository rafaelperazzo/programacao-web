# -*- coding: utf-8 -*-
lista_idade=[]
idade=int(input('Digite a idade:'))
while idade!= -1:
    for i in range(0,idade,1):
        lista_idade.append(idade)
    idade=int(input('Digite a idade:'))
        


    
   

print(lista_idade)