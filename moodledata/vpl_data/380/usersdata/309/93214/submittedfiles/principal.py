# -*- coding: utf-8 -*-
import minha_bib * 
#COMECE AQUI ABAIXO

n=int(input("Digite uma quantidade de notas:"))
   notas = []
    for i in range (0,n,1):
        notas.append(float(input("Digite a nota %d :" %(i+1))))
        print (notas[i])
        
    med=0

    med=sum(notas)/ float(len(notas))
         
    print (med)

