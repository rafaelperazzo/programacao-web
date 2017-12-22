# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO

n=int(input("Digite uma quantidade de notas:"))

if n > 1:
    
    notas = []
    for i in range (0,n,1):
        notas.append(float(input("Digite a nota %d :" %(i+1))))

    med=0

    for i in range (0,n,1):
         med += notas[i]/n
         

    print (notas)
    print (med)

else :
    print("Nota menor q ou igual a 1")
