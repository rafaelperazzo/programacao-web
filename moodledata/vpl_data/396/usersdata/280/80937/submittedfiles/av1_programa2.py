# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n1=int(input("Insira o número 1: "))
n2=int(input("Insira o número 2: "))
n3=int(input("Insira o número 3: "))
n4=int(input("Insira o número 4: "))
n5=int(input("Insira o número 5: "))
n6=int(input("Insira o número 6: "))
s1=int(input("Insira o número sorteado 1: "))
s2=int(input("Insira o número sorteado 2: "))
s3=int(input("Insira o número sorteado 3: "))
s4=int(input("Insira o número sorteado 4: "))
s5=int(input("Insira o número sorteado 5: "))
s6=int(input("Insira o número sorteado 6: "))
x=0
if n1==s1 or n1==s2 or n1==s3 or n1==s4 or n1==s5 or n1==s6:
    x=x+1
if n2==s1 or n2==s2 or n2==s3 or n2==s4 or n2==s5 or n2==s6:
    x=x+1
if n3==s1 or n3==s2 or n3==s3 or n3==s4 or n3==s5 or n3==s6:    
    x=x+1
if n4==s1 or n4==s2 or n4==s3 or n4==s4 or n4==s5 or n4==s6:
    x=x+1
if n5==s1 or n5==s2 or n5==s3 or n5==s4 or n5==s5 or n5==s6:
    x=x+1
if n6==s1 or n6==s2 or n6==s3 or n6==s4 or n6==s5 or n6==s6:
    x=x+1
if x < 3:
    print("azar")
if x == 3:
    print("terno")
if x == 4:
    print("quadra")
if x == 5:
    print("quina")
if x == 6:
    print("sena")