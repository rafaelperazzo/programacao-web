# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO

n=int(input("Digite uma quantidade de notas:"))

if n > 1:
    
    notas = []
    for i in range (0,n,1):
        notas.append(float(input("Digite a nota %d :" %(i+1))))

    med=0

    med=sum(notas)/ float(len(notas))
         

    print (notas)
    print (med)

else :
    print("Nota menor q ou igual a 1")
